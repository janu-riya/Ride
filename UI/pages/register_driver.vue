<template>
    <v-container>
      <driverregister/>
    </v-container>
</template>
<script>
export default {
  layout: 'corporate_layout',
 async mounted () {
  
    this.$vuetify.theme.dark = false
  },
}
</script>
