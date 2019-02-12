import ApiAuth from '../../api_auth'

export default class AccountApi extends ApiAuth {
  static login ({ fields }) {
    return this.unauthPost('/accounts/login/', fields)
  }


  static сlientSignUp ({ fields }) {
    return this.unauthPost('/user/client/', fields)
  }

  static сustomerSignUp ({ fields }) {
    return this.unauthPost('/user/admin/', fields)
  }
}
