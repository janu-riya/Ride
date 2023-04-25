export { default as About } from '../../components/about.vue'
export { default as Bankcorporate } from '../../components/bankcorporate.vue'
export { default as Bankdriver } from '../../components/bankdriver.vue'
export { default as Booking } from '../../components/booking.vue'
export { default as Corporate } from '../../components/corporate.vue'
export { default as Corporatelogin } from '../../components/corporatelogin.vue'
export { default as Corporateprofile } from '../../components/corporateprofile.vue'
export { default as Disquotes } from '../../components/disquotes.vue'
export { default as Distrips } from '../../components/distrips.vue'
export { default as Driverlogin } from '../../components/driverlogin.vue'
export { default as Driverquote } from '../../components/driverquote.vue'
export { default as Driverregister } from '../../components/driverregister.vue'
export { default as Homeintro } from '../../components/homeintro.vue'
export { default as Location } from '../../components/location.vue'
export { default as Profile } from '../../components/profile.vue'
export { default as Profile1 } from '../../components/profile1.vue'
export { default as Quote } from '../../components/quote.vue'
export { default as Register } from '../../components/register.vue'
export { default as Test1 } from '../../components/test1.vue'
export { default as Trip } from '../../components/trip.vue'
export { default as Userlogin } from '../../components/userlogin.vue'
export { default as Vehicle } from '../../components/vehicle.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
