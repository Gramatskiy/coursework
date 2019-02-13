import ApiAuth from '../../api_auth'

export default class AdminApi extends ApiAuth {
    static getProductList({query = ''}) {
        return this.get(`/product/`, query)
    }

    static getProductDetail({id, query = ''}) {
        return this.get(`/product/${id}/`, query)
    }

    static deleteProduct({id}) {
        return this.delete(`/product/${id}/`)
    }

    static updateProduct({id, fields}) {
        return this.patch(`/product/${id}/`, fields)
    }

    static createProduct({fields}) {
        return this.post(`/product/`, fields)
    }

    static getReceiptReceiveList() {
        return this.get(`/receipt/receive/`)
    }

    static getReceiptSellList() {
        return this.get(`/receipt/sell/`)
    }

    static createReceiptReceive({fields}) {
        return this.post(`/receipt/receive/`, fields)
    }

    static createReceiptSold({fields}) {
        return this.post(`/receipt/sell/`, fields)
    }

    static getProductAmountList({id}) {
        return this.get(`/product/${id}/amount/`)
    }

    static getDeviceDetail({id, query = ''}) {
        return this.get(`/device/admin/${id}/`, query)
    }

    static getDeviceStatistics({id, query = ''}) {
        return this.get(`/device/admin/${id}/statistics/`, query)
    }

    static validatePayment() {
        return this.post('/device/admin/validate-payment/')
    }

    static buyDevices({fields}) {
        return this.post(`/device/admin/buy-devices/`, fields)
    }
}
