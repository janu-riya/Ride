<template>
  <v-content>
    <br><br>
   <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">User Login </h1></v-text-title>
      
    <v-container fluid fill-height>
       <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>

                   <v-form>

                      <div class="text-subtitle-1 text-medium-emphasis ">USER PHONE NUMBER</div>

                      <v-text-field
                      v-model="customer.mobile_number"
                        density="compact"
                        placeholder="Mobile Number"
                        prepend-inner-icon="mdi-phone"
                        variant="outlined"
                        :rules="[rules.required,rules.mobile]"
                      ></v-text-field>

                      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">Password</div>

                      <v-text-field
                      v-model="customer.password"
                        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'"
                        density="compact"
                        placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline"
                        variant="outlined"
                        :rules="[rules.required,rules.password]"


                      ></v-text-field>
                      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        <v-btn text color="black" @click="login()">Login</v-btn>
                        <v-btn text color="black" to="/register_user">Register</v-btn>
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
  data: () =>( {
    return: {
      mobile_number: '',
      password: '',
      visible: false,
    },
      

      customer : {
      mobile_number: '',
      password: ''
    },
    rules : {
      required: (v) => !!v || "Required",
            mobile : (v) =>  v.length > 9 || "Minimun 10 Characters is required",
            password : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
    }
  }),
  methods: {
    async login(){
      this.$storage.setUniversal('customer_mobile',this.customer.mobile_number)
      let url = "http://127.0.0.1:8000/customer_login"
      let res = await this.$axios.get(url, { params :{'mobile_number':this.customer.mobile_number, 'password':this.customer.password}})
      console.log(res.data)
      if(res.data == true){
        this.$router.push('/profile_user')
      }
      else{
        console.error('login failed')
      }
    }
  }

};
</script>

<style></style>
