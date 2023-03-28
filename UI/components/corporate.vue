<template>
    <v-content>
      <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">Corporate User Registration </h1></v-text-title>
      <br>
       <v-container fluid fill-height>
          <v-layout align-center justify-center>
             <v-flex xs12 sm8 md5>
                      <v-form>
                        <v-row> <v-col>
                          <div class="text-subtitle-1 text-medium-emphasis">First  name</div>
                        <v-text-field
                          density="compact"
                          v-model="corporate.first_name"
                          placeholder="Enter your first name "
                          prepend-inner-icon="mdi-account-circle"
                          variant="outlined"
                        ></v-text-field>
                      </v-col>
                      
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Last  name</div>
                        <v-text-field
                          density="compact"
                          v-model="corporate.last_name"
                          placeholder="Enter your Last name "
                          prepend-inner-icon="mdi-account-circle"
                          variant="outlined"
                        ></v-text-field>
                      </v-col>
                     </v-row>
                     <v-row>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Firm  name</div>
                        <v-text-field
                          density="compact"
                          v-model="corporate.firm_name"
                          placeholder="Enter your firm name "
                          prepend-inner-icon="mdi-account-circle"
                          variant="outlined"
                        ></v-text-field>
                        </v-col>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Location</div>
  
                        <v-text-field
                        
                          density="compact"
                          v-model="corporate.location"
                          placeholder="Enter the Location"
                          prepend-inner-icon="mdi-account-outline"
                          variant="outlined"
                        ></v-text-field>
                        </v-col>
                     </v-row>
                     
                     <div class="text-subtitle-1 text-medium-emphasis">Email ID</div>
  
                        <v-text-field
                          density="compact"
                          v-model="corporate.email"
                          placeholder="Enter Email ID"
                          prepend-inner-icon="mdi-email-outline"
                          variant="outlined"
                        ></v-text-field>
                   
                      <div class=" text-xl">Provide the Business related Details</div>
                      <br>
                      
                      <v-row>
                        <v-col>
                      <div class="text-1xl">GST number</div>
                      <v-text-field
                        
                        density="compact"
                        v-model="corporate.gst_number"
                          placeholder="Enter the GST Number"
                          prepend-inner-icon="mdi-account-outline"
                          variant="outlined"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <div class="text-1xl">Firm PAN No</div>
                      <v-text-field
                      
                        density="compact"
                        v-model="corporate.firm_pan_no"
                          placeholder="Enter the Firm Pan Number"
                          prepend-inner-icon="mdi-account-outline"
                          variant="outlined"
                      ></v-text-field>
                    </v-col>
                    </v-row>
                    <div  class="text-1xl">Nature Of Business</div>
                   
                    <v-select
                       
                        :items="['others']"
                        label="Select the NAture of Business"
                        v-model="corporate.nature_of_business"
                      ></v-select>
                  
                     <div class="text-subtitle-1 text-medium-emphasis">Password</div>
                        <v-text-field
                          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                          :type="visible ? 'text' : 'password'"
                          density="compact"
                          v-model="corporate.password"
                          placeholder="Enter your password"
                          prepend-inner-icon="mdi-lock-outline"
                          variant="outlined"
  
                        ></v-text-field>
  
                     <v-row>
                      <v-col>
  
                        <div class="text-subtitle-1 text-medium-emphasis">Phone Number</div>
  
                        <v-text-field
                          density="compact"
                          v-model="corporate.mobile_number"
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
                      <br>
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
    data : () => ({
      rules : {
        required : {
          required: (v) => !!v || "Required",

          minimum : (v) =>  v.length == 10 || " 10 Characters is required",
        }
      },
      corporate:{
        first_name : "",
        last_name : "",
        firm_name : "",
        location : "",
        email : "",
        password : "",
        mobile_number : "",
        gst_number : "",
        firm_pan_number : "",
        nature_of_business : "",
      },
      otp:'',
      u_otp:'',
      sendotp : null,
      error : false,

  }),
    methods: {
      async register() {
        let url = "http://127.0.0.1:8000/otp"
            let mdata = { params :{mobile_number : this.corporate.mobile_number}}
            await this.$axios.get(url,mdata).then(res => {
                this.otp = res.data
                this.sendotp = true
                console.log(this.otp)
            }).catch(err => { console.log(err)});
      },
      async signup() {
        if (this.u_otp == this.otp){
      let  url = "http://127.0.0.1:8000/corporate"
      let res= await this.$axios.post(url, this.corporate)
      console.log(res.data)
      
      if(res.data === true){
        this.$router.push('/corporate_bank')
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
  