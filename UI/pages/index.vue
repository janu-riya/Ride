<template>

    <v-sheet fluid height="100%">
      <homeintro/>
      <about/>
      <v-footer color="black">
      
      </v-footer>
    </v-sheet>
    



  
</template>


<script>
export default {
 async mounted () {
    this.$vuetify.theme.dark = false
  },
}
</script>
