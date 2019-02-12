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
              v-model="email.value"
              label="Email"
              :rules="email.rules"
              :error-messages="email.errors"
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
          <v-radio-group v-model="accountType" label="Select account type">
            <v-radio :key="CLIENT" label="Client" :value="CLIENT"></v-radio>
            <v-radio :key="CUSTOMER" label="Admin" :value="CUSTOMER"></v-radio>
          </v-radio-group>
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

const [CLIENT, CUSTOMER] = ['CLIENT', 'CUSTOMER']
export default {
  name: 'SignUp',
  data () {
    return {
      CLIENT,
      CUSTOMER,
      radioGroup: 1,
      registerType: CLIENT,
      nonFieldErrors: [],
      usernameError: 'Username is required',
      username: {
        value: '',
        rules: [
          v => !!v || this.usernameError
        ],
        errors: []
      },
      emailError1: 'Email is required',
      emailError2: 'Write a correct email',

      email: {
        value: '',
        rules: [
          v => !!v || this.emailError1,
          v => /.+@.+/g.test(v) || this.emailError2
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
      accountType: CLIENT
    }
  },
  created () {
    this.$nextTick(() => {
      this.usernameError = this.$translate.text(this.usernameError)
      this.passwordError = this.$translate.text(this.passwordError)
      this.emailError1 = this.$translate.text(this.emailError1)
      this.emailError2 = this.$translate.text(this.emailError2)
    })
  },
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        const fields = {
          username: this.username.value,
          email: this.email.value,
          password: this.password.value
        }
        if (this.accountType === CLIENT) {
          AccountApi.сlientSignUp({ fields })
            .then(response => {
              if (response.status === 201) this.login(fields)
            })
            .catch(reason => this.handleErrors(reason))
        } else if (this.accountType === CUSTOMER) {
          AccountApi.сustomerSignUp({ fields })
            .then(response => {
              if (response.status === 201) this.login(fields)
            })
            .catch(reason => this.handleErrors(reason))
        }
      }
    },
    handleErrors (reason) {
      if (reason.response && reason.response.status === 400) {
        const data = reason.response.data
        this.nonFieldErrors = data['non_field_errors'] || []
        this.username.errors = data['username'] || []
        this.email.errors = data['email'] || []
        this.password.errors = data['password'] || []
      } else {
        console.error(reason.response || reason)
      }
    },
    login (fields) {
      AccountApi.login({ fields })
        .then(response => {
          // gets token from data, sets it in localstorage and store, sets is_client and is_admin as well
          const data = response.data
          if (data.token) {
            this.removeUser()
            this.setJSONWebToken(data.token)
            if (data.is_client) {
              this.removeIsAdmin()
              this.setIsProvider(true)
              if (data.is_premium) {
                this.setIsPremium(true)
              } else {
                this.removeIsPremium()
              }
              this.$router.push({ 'name': 'client' })
            } else if (data.is_admin) {
              this.removeIsClient()
              this.removeIsPremium()
              this.setIsAdmin(true)
              this.$router.push({ 'name': 'admin' })
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
