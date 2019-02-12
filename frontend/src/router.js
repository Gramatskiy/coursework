import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

import SignIn from './views/accounts/SignIn.vue'
import SignUp from './views/accounts/SignUp.vue'

import SubscribePremium from './views/clients/SubscribePremium.vue'
import ClientDeviceStatistics from './views/clients/DeviceStatistics'
import Client from './views/clients/Index'
import ClientMap from './views/clients/Map'

import Admin from './views/admin/Index'
import AdminProducts from './views/admin/Products'
import AdminDeviceStatistics from './views/admin/DeviceStatistics'
import AdminUpdateProduct from './views/admin/UpdateProduct'
import AdminCreateProduct from './views/admin/CreateProduct'

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
        path: '/provider/invoice',
        name: 'provider-invoice',
        component: Client,
        redirect: '/provider/invoice/',
        meta: {'requireClient': true},
        children: [
            {
                path: 'dashboard/',
                name: 'client-dashboard',
                component: ClientMap,
                meta: {'menuItemName': 'dashboard'}
            },
            {
                path: 'subscribe-premium/',
                name: 'subscribe-premium',
                component: SubscribePremium
            },
            {
                path: '/device/:id/statistics/',
                name: 'client-device-statistics',
                component: ClientDeviceStatistics,
                beforeEnter(to, from, next) {
                    if (!(isPremium())) {
                        next({'name': 'client'})
                    }
                    next()
                },
                props: true
            }

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
                path: '/buy-device/',
                name: 'admin-buy-device',
                component: AdminDeviceStatistics,
                props: true
            }
        ]
    }
]

const router = new Router({
    routes,
    mode: 'history'
})

function isLoggedIn() {
    return store.getters.isLoggedIn
}

function isClient() {
    return store.getters.isClient
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
        // check that user is logged and is client or admin
        if (!isLoggedIn() || !(isClient() || isAdmin())) {
            next({name: 'sign-in'})
        } else {
            // every router that inherits from /admin/ has admin meta in root matched path
            if (to.matched.some(record => record.meta.requireAdmin)) {
                // continue if admin goes admin's route
                if (isAdmin()) {
                    next()
                } else if (isClient()) {
                    next({name: 'client'})
                }
            } else if (to.matched.some(record => record.meta.requireClient)) {
                // continue if client goes client's route
                if (isClient()) {
                    if (to.name === 'subscribe-premium') {
                        if (!isPremium()) {
                            next()
                        } else {
                            next({name: 'client'})
                        }
                    }
                    next()
                } else if (isAdmin()) {
                    next({name: 'admin'})
                }
            } else if (isAdmin()) {
                next({name: 'admin'})
            } else if (isClient()) {
                next({name: 'client'})
            } else {
                throw new InvalidUserError()
            }
        }
    }
})
export default router
