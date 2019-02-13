import axios from 'axios/index'
import { DOMAIN } from './constants'
import store from './store'
import router from './router'

let request = axios.create()

request.defaults.xsrfCookieName = 'csrftoken';
request.defaults.xsrfHeaderName = 'X-CSRFToken';

export default class ApiAuth {
  static getAuthConfig () {
    return {
      headers: {
        'Authorization': `JWT ${localStorage.getItem('JSONWebToken')}`
      }
    }
  }

  static __clearAndRedirectToSignIn () {
    const dispatch = store.dispatch;
    dispatch('removeJSONWebToken');
    dispatch('removeUser');
    dispatch('removeIsProvider');
    dispatch('removeIsAdmin');
    router.push({ 'name': 'sign-in' })
  }

  static checkAuth (promise) {
    // check that token is not expired
    const exp = (new Date(localStorage.getItem('JSONWebTokenExpiration')) - new Date()) / (1000 * 60 * 60 * 24)
    if (exp < 1 && exp > 0) {
      request.post(DOMAIN + '/token-refresh/', { 'token': localStorage.getItem('JSONWebToken') })
        .then(response => {
          store.dispatch('setJSONWebToken', response.data.token)
          console.info('New token has been set')
        })
        .catch(reason => {
          console.error(reason.response || reason)
          this.__clearAndRedirectToSignIn()
        })
    }
    return promise.catch(reason => {
      const status = reason.response && reason.response.status
      if (status === 401) {
        this.__clearAndRedirectToSignIn()
      } else {
        throw reason
      }
    })
  }

  // post wrapper
  static post (url, payload) {
    return this.checkAuth(request.post(DOMAIN + url, payload, this.getAuthConfig()))
  }

  // get wrapper
  static get (url, query = '') {
    return this.checkAuth(request.get(DOMAIN + url + query, this.getAuthConfig()))
  }

  // put wrapper
  static put (url, payload) {
    return this.checkAuth(request.put(DOMAIN + url, payload, this.getAuthConfig()))
  }

  // patch wrapper
  static patch (url, payload) {
    return this.checkAuth(request.patch(DOMAIN + url, payload, this.getAuthConfig()))
  }

  // delete wrapper
  static delete (url) {
    return this.checkAuth(request.delete(DOMAIN + url, this.getAuthConfig()))
  }

  // options wrapper
  static options (url) {
    return this.checkAuth(request.options(DOMAIN + url, this.getAuthConfig()))
  }

  static unauthPost (url, payload) {
    return request.post(DOMAIN + url, payload)
  }

  // get with with already full url
  static domainGet (url, query = '') {
    return this.checkAuth(request.get(url + query, this.getAuthConfig()))
  }
}
