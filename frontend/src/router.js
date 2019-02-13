import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

import SignIn from './views/accounts/SignIn.vue'
import SignUp from './views/accounts/SignUp.vue'


import Provider from './views/providers/Index'

import Admin from './views/admin/Index'
import AdminProducts from './views/admin/Products'
import AdminUpdateProduct from './views/admin/UpdateProduct'
import AdminCreateProduct from './views/admin/CreateProduct'
import AdminReceiptReceiveList from './views/admin/ReceiptReceiveList'
import AdminReceiptSellList from './views/admin/ReceiptSellList'
import AdminReceiptReceiveCreate from './views/admin/ReceiptReceiveCreate'
import AdminReceiptSellCreate from './views/admin/ReceiptSellCreate'
import AdminProductAmounStatistics from './views/admin/ProductAmounStatistics'

import InvalidUserError from './errors'

Vue.use(Router);

const routes = [
    {
        path: '/sign-in/',
        name: 'sign-in',
        component: SignIn
    },
    {
        path: '/sign-up/',
        name: 'sign-up',
        component: SignUp
    },
    {
        path: '/providers',
        name: 'providers',
        component: Provider,
        redirect: '/providers/receipt/receive/',
        meta: {'requireProvider': true},
        children: [
            {
                path: 'receipt/receive/',
                name: 'providers-receipt-receive-create',
                component: AdminReceiptReceiveCreate,
                props: true
            },

        ]
    },
    {
        path: '/admin',
        name: 'admin',
        component: Admin,
        redirect: '/admin/product/',
        meta: {'requireAdmin': true},
        children: [
            {
                path: 'product/',
                name: 'admin-dashboard',
                component: AdminProducts,
                meta: {'menuItemName': 'dashboard'}
            },
            {
                path: 'product/create/',
                name: 'admin-product-create',
                component: AdminCreateProduct,
                props: true
            },
            {
                path: 'product/:id/',
                name: 'admin-product-update',
                component: AdminUpdateProduct,
                props: true
            },
            {
                path: 'receipt/receive/',
                name: 'admin-receipt-receive',
                component: AdminReceiptReceiveList,
                props: true
            },
            {
                path: 'receipt/sell/',
                name: 'admin-receipt-sell',
                component: AdminReceiptSellList,
                props: true
            }, {
                path: 'receipt/receive/create/',
                name: 'admin-receipt-receive-create',
                component: AdminReceiptReceiveCreate,
                props: true
            }, {
                path: 'receipt/sell/create/',
                name: 'admin-receipt-sell-create',
                component: AdminReceiptSellCreate,
                props: true
            }, {
                path: 'product/:id/amount/',
                name: 'admin-product-amount',
                component: AdminProductAmounStatistics,
                props: true
            },
        ]
    }
];

const router = new Router({
    routes,
    mode: 'history'
})

function isLoggedIn() {
    return store.getters.isLoggedIn
}

function isProvider() {
    return store.getters.isProvider
}

function isAdmin() {
    return store.getters.isAdmin
}

function isPremium() {
    return store.state.isPremium
}

router.beforeEach((to, from, next) => {
    if (['sign-in', 'sign-up', 'reset-password', 'set-password'].indexOf(to.name) !== -1) {
        next()
    } else {
        // check that user is logged and is providers or admin
        if (!isLoggedIn() || !(isProvider() || isAdmin())) {
            next({name: 'sign-in'})
        } else {
            // every router that inherits from /admin/ has admin meta in root matched path
            if (to.matched.some(record => record.meta.requireAdmin)) {
                // continue if admin goes admin's route
                if (isAdmin()) {
                    next()
                } else if (isProvider()) {
                    next({name: 'providers'})
                }
            } else if (to.matched.some(record => record.meta.requireProvider)) {
                // continue if providers goes providers's route
                if (isProvider()) {
                    if (to.name === 'subscribe-premium') {
                        if (!isPremium()) {
                            next()
                        } else {
                            next({name: 'providers'})
                        }
                    }
                    next()
                } else if (isAdmin()) {
                    next({name: 'admin'})
                }
            } else if (isAdmin()) {
                next({name: 'admin'})
            } else if (isProvider()) {
                next({name: 'providers'})
            } else {
                throw new InvalidUserError()
            }
        }
    }
})
export default router
