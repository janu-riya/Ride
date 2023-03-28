<template>
  <v-content>
    <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">User Register </h1></v-text-title>
    <br>
     <v-container fluid fill-height>
        <v-layout align-center justify-center>
           <v-flex xs12 sm8 md5>
                    <v-form>
                      <v-row> <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">First  name</div>
                      <v-text-field
                        density="compact"
                        v-model="customer.first_name"
                        placeholder="Enter your first name "
                        prepend-inner-icon="mdi-account-circle"
                        variant="outlined"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    
                    <v-col>
                      <div class="text-subtitle-1 text-medium-emphasis">Last  name</div>
                      <v-text-field
                      v-model="customer.last_name"
                        density="compact"
                        placeholder="Enter your first name "
                        prepend-inner-icon="mdi-account-circle"
                        variant="outlined"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                   </v-row>
                   <div class="text-subtitle-1 text-medium-emphasis">Location</div>

                      <v-text-field
                      v-model="customer.location"
                        density="compact"
                        placeholder="Enter the Location"
                        prepend-inner-icon="mdi-account-outline"
                        variant="outlined"
                        :rules="[rules.required]"
                      ></v-text-field>
                   <div class="text-subtitle-1 text-medium-emphasis">Aadhar ID</div>

                      <v-text-field
                      v-model="customer.aadhar_id"
                        density="compact"
                        placeholder="Enter Aadhar ID"
                        prepend-inner-icon="mdi-account-outline"
                        variant="outlined"
                        :rules="[rules.required]"
                      ></v-text-field>
                      <v-radio-group
                      v-model="customer.userType"
                      label=""
                      :rules="[rules.required]"
                      row
                    >
                    <v-radio
                      label="Select Whether you running a business as a Firm"
                      value="Business user"
                    ></v-radio>
                      </v-radio-group>
                    <div v-if="customer.userType === 'Business user'" class=" text-xl">Provide the Business related Details</div>
                    
                    <v-row>
                      <v-col>
                    <div v-if="customer.userType === 'Business user'" class="text-1xl">GST number</div>
                    <v-text-field
                      v-if="customer.userType === 'Business user'"
                      v-model="customer.gst_number"
                      density="compact"
                        placeholder="Enter the GST Number"
                        prepend-inner-icon="mdi-account-outline"
                        variant="outlined"
                        :rules="[rules.required]"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <div v-if="customer.userType === 'Business user'" class="text-1xl">Firm PAN No</div>
                    <v-text-field
                      v-if="customer.userType === 'Business user'"
                      v-model="customer.firm_pan_no"
                      density="compact"
                        placeholder="Enter the Firm Pan Number"
                        prepend-inner-icon="mdi-account-outline"
                        variant="outlined"
                        :rules="[rules.required]"
                    ></v-text-field>
                  </v-col>
                  </v-row>
                  <div v-if="customer.userType === 'Business user'" class="text-1xl">Nature Of Business</div>
                 
                  <v-select
                  v-if="customer.userType === 'Business user'"
                     v-model="customer.nature_of_business"
                      :items="['others']"
                      label="Select the NAture of Business"
                      :rules="[rules.required]"
                    ></v-select>
                
                   <div class="text-subtitle-1 text-medium-emphasis">Password</div>
                      <v-text-field
                        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'"
                        density="compact"
                        v-model="customer.password"
                        placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline"
                        variant="outlined"
                        :rules="[rules.required]"

                      ></v-text-field>

                   <v-row>
                    <v-col>

                      <div class="text-subtitle-1 text-medium-emphasis">Phone Number</div>

                      <v-text-field
                        density="compact"
                        v-model="customer.mobile_number"
                        placeholder="Enter the phone number"
                        prepend-inner-icon="mdi-phone"
                        variant="outlined"
                        :rules="[rules.required, rules.minimum]"
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

      customer : {
        first_name:'',
        last_name:'',
        location:'',
        aadhar_id:'',
        userType:'',
        gst_number:'',
        firm_pan_no:'',
        password:'',
        mobile_number:'',
        nature_of_business:'',
      },
      otp : '',
      u_otp:'',
      sendotp : null,
      error : false,

  }),
  methods: {
    async register() {
      let url = "http://127.0.0.1:8000/otp"
            let mdata = { params :{mobile_number : this.customer.mobile_number}}
            await this.$axios.get(url,mdata).then(res => {
                this.otp = res.data
                this.sendotp = true
                console.log(this.otp)
            }).catch(err => { console.log(err)});
     
    },
    async signup() {
      if (this.u_otp == this.otp){
      let  url = "http://127.0.0.1:8000/customer"
      let res= await this.$axios.post(url, this.customer)
      console.log(res.data)
      
      if(res.data === true){
        this.$router.push('/loginuser')
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
