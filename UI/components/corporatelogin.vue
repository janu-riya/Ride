<template>
    <v-content>
      <br><br>
      <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">Corporate Login </h1></v-text-title>
      
      <v-container fluid fill-height>
         <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>

                     <v-form>
                      <div class="text-subtitle-1 text-medium-emphasis">User phone number</div>

                      <v-text-field
                      v-model="corporate.mobile_number"
                        density="compact"
                        placeholder="Enter Phone Number "
                        prepend-inner-icon="mdi-phone-outline"
                        variant="outlined"
                      ></v-text-field>

                      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Password</div>

                      <v-text-field
                      v-model="corporate.password"
                        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'"
                        density="compact"
                        placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline"
                        variant="outlined"

                      ></v-text-field>
                      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        
                        <v-btn text color="black" @click="login()">Login</v-btn>
                        <v-btn text color="black" to="/corporate_register">Register</v-btn>
                        
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
  data() {
    return {
      mobile_number: '',
      password: '',
      corporate:{
        mobile_number: '',
        password: '',
      }
    }
  },
methods:{
  async login(){
    this.$storage.setUniversal('corporate_mobile',this.corporate.mobile_number)
    let url = "http://127.0.0.1:8000/corporate_login"
      let res = await this.$axios.get(url, { params :{mobile_number: this.corporate.mobile_number, password:this.corporate.password}})
      console.log(res.data)
      if(res.data == true){
        this.$router.push('/corporate_profile')
      }
      else{
        console.error('login failed')
      }
  }

  }
};
</script>

<style></style>
