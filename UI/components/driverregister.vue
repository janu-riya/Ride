<template>
  
  <v-content class="mx-auto">
    <v-text-title class="mx-auto"><h1 style="text-align: center;" class="font-bold text-3xl">Driver Register </h1></v-text-title>
    <br>
     <v-container fluid fill-height class="mx-auto">
        <v-layout align-center justify-center class="mx-auto">
           <v-flex xs12 sm8 md5 class="mx-auto">
                    <v-form class="mx-auto">
                      <v-row> <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">First  name</div>
                      <v-text-field
                        density="compact"
                        v-model="driver.first_name"
                        placeholder="Enter your first name "
                        prepend-inner-icon="mdi-account-circle"
                        variant="outlined"
                      ></v-text-field>
                    </v-col>
                    
                    <v-col>
                      <div class="text-subtitle-1 text-medium-emphasis">Last  name</div>
                      <v-text-field
                        density="compact"
                        v-model="driver.last_name"
                        placeholder="Enter your first name "
                        prepend-inner-icon="mdi-account-circle"
                        variant="outlined"
                      ></v-text-field>
                    </v-col>
                   </v-row>
                   <v-row>
                    <v-col>
                      <div class="text-subtitle-1 text-medium-emphasis">Location</div>

                      <v-text-field
                        density="compact"
                        v-model="driver.location"
                        placeholder="Enter the Location"
                        prepend-inner-icon="mdi-account-outline"
                        variant="outlined"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <div class="text-subtitle-1 text-medium-emphasis">Aadhar ID</div>

                      <v-text-field
                        density="compact"
                        v-model="driver.aadhar_id"
                        placeholder="Enter Aadhar ID"
                        prepend-inner-icon="mdi-account-outline"
                        variant="outlined"
                      ></v-text-field>
                    </v-col>
                   </v-row>
                   <v-row>
                    <v-col>
                      <div class="text-subtitle-1 text-medium-emphasis">Password</div>
                      <v-text-field
                        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'"
                        density="compact"
                        v-model="driver.password"
                        placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline"
                        variant="outlined"

                      ></v-text-field>
                    </v-col>
                    <v-col>

                      <div class="text-subtitle-1 text-medium-emphasis">Phone Number</div>

                      <v-text-field
                        density="compact"
                        v-model="driver.mobile_number"
                        placeholder="Enter the phone number"
                        prepend-inner-icon="mdi-phone"
                        variant="outlined"
                      ></v-text-field>
                    </v-col>
                    </v-row>
                    <v-row>
                      <v-spacer></v-spacer>
                      <v-btn text color="black" @click="register()">SUBMIT</v-btn>
                      <v-spacer></v-spacer>
                    </v-row>  
                    
                    </v-form>
                    <v-container v-if="sendotp">
                      <v-form>
                          <v-alert v-model="error" type="error"  dismissible>OTP verification failed</v-alert>
                          <v-col>
                              <v-row>
                                  <caption> An OTP is send to your provided email. Please enter the OTP below for verification</caption>
                              </v-row>
                              <v-row>
                                  <v-text-field label ="Enter OTP Here" v-model="u_otp"></v-text-field>
                              </v-row>
                              <v-row>
                                  <v-btn large block color="indigo darken-3" @click="signup()" class="button">signup</v-btn>
                              </v-row>
                          </v-col>
                      </v-form>
                  </v-container>


           </v-flex>
        </v-layout>
     </v-container>
  </v-content>
</template>
<script>
export default {
  data() {
    return  {
      driver :{
      corporate_mobile:this.$storage.getUniversal('corporate_mobile') ,
      first_name : "",
      last_name : "",
      location : "",
      aadhar_id : "",
      userType : "",
      password : "",
      mobile_number : "",
      gst_number : "",
      firm_pan_number : "",
      natureof_business : "",
    },
    otp : '',
      u_otp:'',
      sendotp : null,
      error : false,
    }
  },
  methods: {
    async register() {
      let url = "http://127.0.0.1:8000/otp"
            let mdata = { params :{mobile_number : this.driver.mobile_number}}
            await this.$axios.get(url,mdata).then(res => {
                this.otp = res.data
                this.sendotp = true
                console.log(this.otp)
            }).catch(err => { console.log(err)});
    },
    async signup(){
      if (this.u_otp == this.otp){
      let  url = "http://127.0.0.1:8000/driver"
      let res= await this.$axios.post(url, this.driver)
      console.log(res.data)
      
      if(res.data === true){
        this.$router.push('/driverbank')
            }
      else{
        console.error("register failed");
      }
    }
    else{
      this.error = true;
    }
    }
  }
}
</script>


<style></style>