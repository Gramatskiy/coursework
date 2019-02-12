<template>
  <v-app>
    <v-layout align-center justify-center fill-height>
      <v-flex xs12 sm6 lg3 pa-2>
        <ul v-if="nonFieldErrors.length > 0">
          <li v-for="(error, ind) in nonFieldErrors" :key="ind">{{error}}</li>
        </ul>
        <v-form ref="form" @submit.prevent="submit">
          <v-text-field
            v-model="username.value"
            label="Username"
            :rules="username.rules"
            required
          ></v-text-field>
          <v-text-field
            v-model="password.value"
            :append-icon="password.show ? 'visibility_off' : 'visibility'"
            :type="password.show ? 'text' : 'password'"
            label="Password"
            :rules="password.rules"
            @click:append="password.show = !password.show"
          ></v-text-field>

          <v-layout justify-space-between>
            <v-layout class="subheading font-weight-thin" align-center>
              <div class="mr-1">{{t('Don\'t have an account?')}}</div>
              <router-link :to="{'name':'sign-up'}">{{t(' Sign up')}}</router-link>
            </v-layout>
            <v-btn color="success" type="submit">{{t('Sign in')}}</v-btn>
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
    name: 'SignIn',
    data() {
      return {
        nonFieldErrors: [],
        usernameError: 'Username is required',
        username: {
          value: '',
          rules: [
            v => !!v || this.usernameError
          ]
        },

        passwordError: 'Password is required',
        password: {
          value: '',
          rules: [
            v => v.length > 0 || this.passwordError
          ],
          show: false
        }
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
          }
          AccountApi.login({fields})
            .then(response => {
              // gets token from data, sets it in localstorage and store, sets is_client and is_admin as well
              const data = response.data
              if (data.token) {
                this.removeUser();
                this.setJSONWebToken(data.token);
                if (data.is_provider) {
                  this.removeIsAdmin();
                  this.setIsProvider(true);
                  if (data.is_premium) {
                    this.setIsPremium(true)
                  } else {
                    this.removeIsPremium()
                  }
                  this.$router.push({'name': 'client'})
                } else if (data.is_admin) {
                  this.removeIsClient()
                  this.removeIsPremium()
                  this.setIsAdmin(true)
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
  }
</script>

<style scoped>

</style>
