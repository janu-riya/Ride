import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _5dc2e007 = () => interopDefault(import('../pages/corporate_bank.vue' /* webpackChunkName: "pages/corporate_bank" */))
const _221ba9ae = () => interopDefault(import('../pages/corporate_profile.vue' /* webpackChunkName: "pages/corporate_profile" */))
const _753cab6e = () => interopDefault(import('../pages/corporate_register.vue' /* webpackChunkName: "pages/corporate_register" */))
const _0a9fd67a = () => interopDefault(import('../pages/driver_profile.vue' /* webpackChunkName: "pages/driver_profile" */))
const _8d3f8bd6 = () => interopDefault(import('../pages/driverbank.vue' /* webpackChunkName: "pages/driverbank" */))
const _5b280366 = () => interopDefault(import('../pages/logincorporate.vue' /* webpackChunkName: "pages/logincorporate" */))
const _5ec64af0 = () => interopDefault(import('../pages/logindriver.vue' /* webpackChunkName: "pages/logindriver" */))
const _459f6113 = () => interopDefault(import('../pages/loginuser.vue' /* webpackChunkName: "pages/loginuser" */))
const _09ace392 = () => interopDefault(import('../pages/profile_user.vue' /* webpackChunkName: "pages/profile_user" */))
const _59602263 = () => interopDefault(import('../pages/register_driver.vue' /* webpackChunkName: "pages/register_driver" */))
const _78c30d74 = () => interopDefault(import('../pages/register_user.vue' /* webpackChunkName: "pages/register_user" */))
const _33acc900 = () => interopDefault(import('../pages/ride_now.vue' /* webpackChunkName: "pages/ride_now" */))
const _619fc1c0 = () => interopDefault(import('../pages/vehicle_reg.vue' /* webpackChunkName: "pages/vehicle_reg" */))
const _2d8d709e = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/corporate_bank",
    component: _5dc2e007,
    name: "corporate_bank"
  }, {
    path: "/corporate_profile",
    component: _221ba9ae,
    name: "corporate_profile"
  }, {
    path: "/corporate_register",
    component: _753cab6e,
    name: "corporate_register"
  }, {
    path: "/driver_profile",
    component: _0a9fd67a,
    name: "driver_profile"
  }, {
    path: "/driverbank",
    component: _8d3f8bd6,
    name: "driverbank"
  }, {
    path: "/logincorporate",
    component: _5b280366,
    name: "logincorporate"
  }, {
    path: "/logindriver",
    component: _5ec64af0,
    name: "logindriver"
  }, {
    path: "/loginuser",
    component: _459f6113,
    name: "loginuser"
  }, {
    path: "/profile_user",
    component: _09ace392,
    name: "profile_user"
  }, {
    path: "/register_driver",
    component: _59602263,
    name: "register_driver"
  }, {
    path: "/register_user",
    component: _78c30d74,
    name: "register_user"
  }, {
    path: "/ride_now",
    component: _33acc900,
    name: "ride_now"
  }, {
    path: "/vehicle_reg",
    component: _619fc1c0,
    name: "vehicle_reg"
  }, {
    path: "/",
    component: _2d8d709e,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
