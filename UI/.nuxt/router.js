import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _0dd3b432 = () => interopDefault(import('../pages/assigned_quotes.vue' /* webpackChunkName: "pages/assigned_quotes" */))
const _732de29c = () => interopDefault(import('../pages/corporate_bank.vue' /* webpackChunkName: "pages/corporate_bank" */))
const _dc05ba0e = () => interopDefault(import('../pages/corporate_profile.vue' /* webpackChunkName: "pages/corporate_profile" */))
const _018a5b83 = () => interopDefault(import('../pages/corporate_register.vue' /* webpackChunkName: "pages/corporate_register" */))
const _101b1758 = () => interopDefault(import('../pages/driver_profile.vue' /* webpackChunkName: "pages/driver_profile" */))
const _2c75cf2a = () => interopDefault(import('../pages/driverbank.vue' /* webpackChunkName: "pages/driverbank" */))
const _2dbfc931 = () => interopDefault(import('../pages/drivers_quotes.vue' /* webpackChunkName: "pages/drivers_quotes" */))
const _3051fe3c = () => interopDefault(import('../pages/logincorporate.vue' /* webpackChunkName: "pages/logincorporate" */))
const _4e63587b = () => interopDefault(import('../pages/logindriver.vue' /* webpackChunkName: "pages/logindriver" */))
const _d8af5544 = () => interopDefault(import('../pages/loginuser.vue' /* webpackChunkName: "pages/loginuser" */))
const _0db18767 = () => interopDefault(import('../pages/profile_user.vue' /* webpackChunkName: "pages/profile_user" */))
const _411cc886 = () => interopDefault(import('../pages/quotes.vue' /* webpackChunkName: "pages/quotes" */))
const _1d551b24 = () => interopDefault(import('../pages/register_driver.vue' /* webpackChunkName: "pages/register_driver" */))
const _402e5011 = () => interopDefault(import('../pages/register_user.vue' /* webpackChunkName: "pages/register_user" */))
const _c3491c56 = () => interopDefault(import('../pages/ride_now.vue' /* webpackChunkName: "pages/ride_now" */))
const _12d73cd8 = () => interopDefault(import('../pages/test.vue' /* webpackChunkName: "pages/test" */))
const _5931c907 = () => interopDefault(import('../pages/user_book.vue' /* webpackChunkName: "pages/user_book" */))
const _78c79562 = () => interopDefault(import('../pages/user_requests.vue' /* webpackChunkName: "pages/user_requests" */))
const _40492540 = () => interopDefault(import('../pages/user_trips.vue' /* webpackChunkName: "pages/user_trips" */))
const _8265a6aa = () => interopDefault(import('../pages/vehicle_reg.vue' /* webpackChunkName: "pages/vehicle_reg" */))
const _60e6197c = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/assigned_quotes",
    component: _0dd3b432,
    name: "assigned_quotes"
  }, {
    path: "/corporate_bank",
    component: _732de29c,
    name: "corporate_bank"
  }, {
    path: "/corporate_profile",
    component: _dc05ba0e,
    name: "corporate_profile"
  }, {
    path: "/corporate_register",
    component: _018a5b83,
    name: "corporate_register"
  }, {
    path: "/driver_profile",
    component: _101b1758,
    name: "driver_profile"
  }, {
    path: "/driverbank",
    component: _2c75cf2a,
    name: "driverbank"
  }, {
    path: "/drivers_quotes",
    component: _2dbfc931,
    name: "drivers_quotes"
  }, {
    path: "/logincorporate",
    component: _3051fe3c,
    name: "logincorporate"
  }, {
    path: "/logindriver",
    component: _4e63587b,
    name: "logindriver"
  }, {
    path: "/loginuser",
    component: _d8af5544,
    name: "loginuser"
  }, {
    path: "/profile_user",
    component: _0db18767,
    name: "profile_user"
  }, {
    path: "/quotes",
    component: _411cc886,
    name: "quotes"
  }, {
    path: "/register_driver",
    component: _1d551b24,
    name: "register_driver"
  }, {
    path: "/register_user",
    component: _402e5011,
    name: "register_user"
  }, {
    path: "/ride_now",
    component: _c3491c56,
    name: "ride_now"
  }, {
    path: "/test",
    component: _12d73cd8,
    name: "test"
  }, {
    path: "/user_book",
    component: _5931c907,
    name: "user_book"
  }, {
    path: "/user_requests",
    component: _78c79562,
    name: "user_requests"
  }, {
    path: "/user_trips",
    component: _40492540,
    name: "user_trips"
  }, {
    path: "/vehicle_reg",
    component: _8265a6aa,
    name: "vehicle_reg"
  }, {
    path: "/",
    component: _60e6197c,
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
