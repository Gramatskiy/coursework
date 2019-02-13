import ApiAuth from '../../api_auth'

export default class PremiumClientApi extends ApiAuth {
  static getDeviceList ({ query = '' }) {
    return this.get(`/device/client/premium/`, query)
  }

  static getDeviceDetail ({ id, query = '' }) {
    return this.get(`/device/client/premium/${id}/`, query)
  }

  static getDeviceStatistics ({ id, query = '' }) {
    return this.get(`/device/client/premium/${id}/statistics/`, query)
  }
}
