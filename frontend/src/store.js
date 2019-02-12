import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'
import {
  ADD_SAVED_DEVICE,
  REMOVE_IS_CLIENT,
  REMOVE_IS_CUSTOMER, REMOVE_IS_PREMIUM,
  REMOVE_JWT_TOKEN, REMOVE_SAVED_DEVICE,
  REMOVE_USER,
  SET_ACTIVE_MENU_ITEM_NAME,
  SET_IS_CLIENT,
  SET_IS_CUSTOMER, SET_IS_PREMIUM,
  SET_JWT_TOKEN,
  SET_USER
} from './mutation_types'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    JSONWebToken: localStorage.getItem('JSONWebToken'),
    isAdmin: localStorage.getItem('isAdmin'),
    isClient: localStorage.getItem('isClient'),
    isPremium: localStorage.getItem('isPremium'),
    user: localStorage.getItem('user'),
    activeMenuItemName: null,
    savedDevices: JSON.parse(localStorage.getItem('savedDevices')) || []
  },
  getters: {
    isLoggedIn (state) {
      return !!state.JSONWebToken
    },
    getUser (state) {
      return state.user
    },
    isClient (state) {
      return state.isClient
    },
    isAdmin (state) {
      return state.isAdmin
    },
    isPremium (state) {
      return state.isPremium
    }
  },
  mutations: {
    [SET_JWT_TOKEN] (state, payload) {
      state.JSONWebToken = payload.JSONWebToken
    },
    [REMOVE_JWT_TOKEN] (state) {
      state.JSONWebToken = null
    },
    [SET_IS_CUSTOMER] (state, payload) {
      state.isAdmin = payload.isAdmin
    },
    [REMOVE_IS_CUSTOMER] (state) {
      state.isAdmin = false
    },
    [SET_IS_CLIENT] (state, payload) {
      state.isClient = payload.isClient
    },
    [REMOVE_IS_CLIENT] (state) {
      state.isClient = false
    },
    [SET_IS_PREMIUM] (state, payload) {
      state.isPremium = payload.isPremium
    },
    [REMOVE_IS_PREMIUM] (state) {
      state.isPremium = false
    },
    [SET_USER] (state, payload) {
      state.user = payload
    },
    [REMOVE_USER] (state) {
      state.user = null
    },
    [SET_ACTIVE_MENU_ITEM_NAME] (state, payload) {
      state.activeMenuItemName = payload.activeMenuItemName
    },
    [ADD_SAVED_DEVICE] (state, { deviceId }) {
      if (!state.savedDevices.includes(deviceId)) {
        state.savedDevices.push(deviceId)
        localStorage.setItem('savedDevices', JSON.stringify(state.savedDevices))
      }
    },
    [REMOVE_SAVED_DEVICE] (state, { deviceId }) {
      state.savedDevices = state.savedDevices.filter(d => d !== deviceId)
      localStorage.setItem('savedDevices', JSON.stringify(state.savedDevices))
    }
  },
  actions: {
    setJSONWebToken ({ commit }, token) {
      localStorage.setItem('JSONWebToken', token)
      // get expiration from token
      const payload = jwtDecode(token)
      localStorage.setItem('JSONWebTokenExpiration', new Date(payload['exp'] * 1000))
      commit(SET_JWT_TOKEN, { 'JSONWebToken': token })
    },
    removeJSONWebToken ({ commit }) {
      localStorage.removeItem('JSONWebToken')
      localStorage.removeItem('JSONWebTokenExpiration')
      commit(REMOVE_JWT_TOKEN)
    },
    setIsAdmin ({ commit }, isAdmin) {
      localStorage.setItem('isAdmin', isAdmin)
      commit(SET_IS_CUSTOMER, { 'isAdmin': isAdmin })
    },
    removeIsAdmin ({ commit }) {
      localStorage.removeItem('isAdmin')
      commit(REMOVE_IS_CUSTOMER)
    },
    setIsProvider ({ commit }, isClient) {
      localStorage.setItem('isClient', isClient)
      commit(SET_IS_CLIENT, { 'isClient': isClient })
    },
    removeIsClient ({ commit }) {
      localStorage.removeItem('isClient')
      commit(REMOVE_IS_CLIENT)
    },
    setIsPremium ({ commit }, isPremium) {
      localStorage.setItem('isPremium', isPremium)
      commit(SET_IS_PREMIUM, { 'isPremium': isPremium })
    },
    removeIsPremium ({ commit }) {
      localStorage.removeItem('isPremium')
      commit(REMOVE_IS_PREMIUM)
    },

    setUser ({ commit }, user) {
      localStorage.setItem('user', JSON.stringify(user))
      commit(SET_USER, { 'user': user })
    },
    removeUser ({ commit }) {
      localStorage.removeItem('user')
      commit(REMOVE_USER)
    },

    setActiveMenuItemName ({ commit }, activeMenuItemName) {
      commit(SET_ACTIVE_MENU_ITEM_NAME, { activeMenuItemName })
    },

    addSavedDevice ({ commit }, deviceId) {
      commit(ADD_SAVED_DEVICE, { deviceId })
    },
    removeSavedDevice ({ commit }, deviceId) {
      commit(REMOVE_SAVED_DEVICE, { deviceId })
    }

  }
})
