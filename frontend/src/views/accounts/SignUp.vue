<template>
    <v-app>
        <v-layout align-center justify-center fill-height>
            <v-flex xs12 sm6 lg3 pa-2>
                <v-form ref="form">
                    <v-text-field
                            v-model="username.value"
                            label="Username"
                            :rules="username.rules"
                            :error-messages="username.errors"
                            required
                    ></v-text-field>
                    <v-text-field
                            v-model="password.value"
                            :append-icon="password.show ? 'visibility_off' : 'visibility'"
                            :type="password.show ? 'text' : 'password'"
                            label="Password"
                            :rules="password.rules"
                            :error-messages="password.errors"
                            @click:append="password.show = !password.show"
                    ></v-text-field>
                    <v-layout justify-space-between>
                        <v-layout class="subheading font-weight-thin" align-center>
                            <div class="mr-1">{{t('Already have an account?')}}</div>
                            <router-link :to="{'name':'sign-in'}">{{t(' Sign in')}}</router-link>
                        </v-layout>
                        <v-btn color="success" @click="submit">{{t('Sign up')}}</v-btn>
                    </v-layout>
                </v-form>
            </v-flex>
        </v-layout>
    </v-app>
</template>

<script>
    import AccountApi from './api.js'
    import InvalidUserError from '../../errors'

    export default {
        name: 'SignUp',
        data() {
            return {
                nonFieldErrors: [],
                usernameError: 'Username is required',
                username: {
                    value: '',
                    rules: [
                        v => !!v || this.usernameError
                    ],
                    errors: []
                },
                passwordError: 'Password is required',
                password: {
                    value: '',
                    rules: [
                        v => v.length > 0 || this.passwordError
                    ],
                    errors: [],
                    show: false
                },
            }
        },
        created() {
            this.$nextTick(() => {
                this.usernameError = this.$translate.text(this.usernameError)
                this.passwordError = this.$translate.text(this.passwordError)
            })
        },
        methods: {
            submit() {
                if (this.$refs.form.validate()) {
                    const fields = {
                        username: this.username.value,
                        password: this.password.value
                    };
                    AccountApi.providerSignUp({fields})
                        .then(response => {
                            if (response.status === 201) this.login(fields)
                        })
                        .catch(reason => this.handleErrors(reason))
                }
            },
            handleErrors(reason) {
                if (reason.response && reason.response.status === 400) {
                    const data = reason.response.data
                    this.nonFieldErrors = data['non_field_errors'] || []
                    this.username.errors = data['username'] || []
                    this.password.errors = data['password'] || []
                } else {
                    console.error(reason.response || reason)
                }
            },
            login(fields) {
                AccountApi.login({fields})
                    .then(response => {
                        // gets token from data, sets it in localstorage and store, sets is_client and is_admin as well
                        const data = response.data;
                        if (data.token) {
                            this.removeUser();
                            this.setJSONWebToken(data.token);
                            if (data.is_provider) {
                                this.removeIsAdmin();
                                this.setIsProvider(true);
                                this.$router.push({'name': 'providers'})
                            } else if (data.is_admin) {
                                this.removeIsProvider();
                                this.setIsAdmin(true);
                                this.$router.push({'name': 'admin'})
                            } else {
                                throw new InvalidUserError()
                            }
                        }
                    })
                    .catch(reason => {
                        if (reason.response && reason.response.status === 400) {
                            this.nonFieldErrors = reason.response.data['non_field_errors'] || []
                        } else {
                            console.error(reason.response || reason)
                        }
                    })
            }
        }
    }

</script>

<style scoped>

</style>
