<template>
    <v-content>
      <br><br>
      <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">Driver Login </h1></v-text-title>
      
      <v-container fluid fill-height>
         <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>

                     <v-form>
                      <div class="text-subtitle-1 text-medium-emphasis">DRIVER PHONE NUMBER</div>

                      <v-text-field
                      v-model="driver.mobile_number"
                        density="compact"
                        placeholder="Phone number"
                        prepend-inner-icon="mdi-phone-outline"
                        variant="outlined"
                        :rules="[rules.required, rules.mobile]"
                      ></v-text-field>

                      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Password</div>

                      <v-text-field
                      v-model="driver.password"
                        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'"
                        density="compact"
                        placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline"
                        variant="outlined"
                        :rules="[rules.required, rules.password]"

                      ></v-text-field>
                      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        
                        <v-btn text color="black" @click="login()">Login</v-btn>
                        
                        
                        <v-spacer></v-spacer>

                        <a
                          class="text-caption text-decoration-none text-blue"
                          href="#"
                          rel="noopener noreferrer"
                          target="_blank"
                        >
                       
                          Forgot login password?</a>

                      </div>

                     </v-form>
            </v-flex>
         </v-layout>
      </v-container>
   </v-content>

</template>

<script>
export default {
  data:() =>{
    return {
      mobile_number: '',
      password: '',
      visible: false,
      driver : {
      mobile_number: '',
      password: ''
    },
    rules : {
      required: (v) => !!v || "Required",
            mobile : (v) =>  v.length > 10 || "Minimun 10 Characters is required",
            password : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
    }
  }
  },
methods:{
  async login(){
    this.$storage.setUniversal('driver_mobile', this.driver.mobile_number)
    let url = "http://127.0.0.1:8000/driver_login"
      let res = await this.$axios.get(url, { params :{'mobile_number':this.driver.mobile_number, 'password':this.driver.password}})
      console.log(res.data)
      if(res.data == true){
        this.$router.push('/driver_profile')
      }
      else{
        console.error('login failed')
      }
  }

  }
};
</script>

<style></style>
