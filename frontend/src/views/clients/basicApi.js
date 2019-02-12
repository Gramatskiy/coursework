import ApiAuth from '../../api_auth'

export default class BasicClientApi extends ApiAuth {
  static getDeviceList ({ query = '' }) {
    return this.get(`/device/client/`, query)
  }

  static validatePayment () {
    return this.post('/clients/validate-payment/', {})
  }

  static makeClientPremium ({ token }) {
    return this.post(`/clients/make-premium/${token}/`, {})
  }
}
