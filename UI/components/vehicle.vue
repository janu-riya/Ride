<template>
    <v-content>
      <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">Vehicle Registration </h1></v-text-title>
      <br>
       <v-container fluid fill-height>
          <v-layout align-center justify-center>
             <v-flex xs12 sm8 md5>
                      <v-form>
                        <v-row> <v-col>
                          <div class="text-subtitle-1 text-medium-emphasis">Owner name</div>
                        <v-text-field
                          density="compact"
                          v-model="vehicle.owner_name"
                          placeholder="Enter your name "
                          prepend-inner-icon="mdi-account-circle"
                          variant="outlined"
                          :rules="[rules.required]"
                        ></v-text-field>
                      </v-col>
                      
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Supplier Type</div>
                    <v-select
                    v-model="vehicle.supplier_type"
                      label="Select"
                      :items="['INDIVIDUAL', 'BUSINESS']"
                    ></v-select>
                      </v-col>
                     </v-row>
                     <v-row>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Vehicle Type</div>
                    <v-select
                    v-model="vehicle.vehicle_type"
                      label="Select"
                      :items="['Car-Sedan', 'Car-hatchback','Car-SUV','Car-VAN','Bike','Auto']"
                    ></v-select>
                        </v-col>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Fuel Type</div>
                                <v-select
                                v-model="vehicle.fuel_type"
                                label="Select"
                                :items="['Petrol', 'Diesel','Electricity','LPG']"
                                ></v-select>
                        </v-col>
                     </v-row>
                     <v-row>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Vehicle Capacity</div>
                                <v-select
                                v-model="vehicle.vehicle_capacity"
                                label="Select"
                                :items="['1', '3','4','7','9']"
                                ></v-select>
                        </v-col>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Registration number</div>
  
                            <v-text-field
                            v-model="vehicle.registration_no"
                              density="compact"
                              placeholder="Enter Vehicle Registration number"
                              prepend-inner-icon="mdi-account-outline"
                              variant="outlined"
                              :rules="[rules.required]"
                            ></v-text-field>
                        </v-col>
                     </v-row>
                     <br>
                     <div class="text-title-1 text-xl text-medium-emphasis">Road Permit Detail</div>
                     <br>
                     <v-row>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Insurance number</div>
  
                            <v-text-field
                            v-model="vehicle.insurance_no"
                              density="compact"
                              placeholder="Insurance Number"
                              prepend-inner-icon="mdi-account-outline"
                              variant="outlined"
                              :rules="[rules.required]"
                            ></v-text-field>
                        </v-col>
                        <v-spacer></v-spacer>
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Issue Date</div>
                            
                            <input style="padding-top: 7%;"  type="date" v-model="vehicle.issue_date" :rules="[v => !!v || 'Date is required']">
                        </v-col>
                        
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Expiry Date</div>
                            
                            <input style="padding-top: 7%;"    type="date" v-model="vehicle.expiry_date" :rules="[v => !!v || 'Date is required']">
                        </v-col>
                     </v-row>
                     <v-row>
                      <div class="text-subtitle-1 text-medium-emphasis">Agency Mobile Number</div>
  
                            <v-text-field
                            v-model="vehicle.mobile_number"
                              density="compact"
                              placeholder="Enter Vehicle Registration number"
                              prepend-inner-icon="mdi-account-outline"
                              variant="outlined"
                              :rules="[rules.required]"
                            ></v-text-field>
                     </v-row>
                     <br>
                     <div class="text-title-1 text-xm text-medium-emphasis">Upload the documents(Insurance, Fitness, RC book)</div>
                     <v-row>
                        
                        <v-col>
                            
                            <v-file-input label="upload here"></v-file-input>
                        </v-col>
                        
                        <v-col style="padding-top: 3%; padding-left:20%;">

                            <v-btn   color="black darken-3" text outlined @click="submitFiles()">Upload</v-btn>
                        </v-col>
    
                     </v-row>
                     </v-form>
                     <br>
                     
                     
                        <v-form>
                                <v-row justify="center">
                                    <v-btn   color="black darken-3"  text @click="submit()">Submit</v-btn>
                                </v-row>
                        </v-form>
  
  
             </v-flex>
          </v-layout>
       </v-container>
   
    </v-content>
  </template>
  <script>

  export default {
    data(){
        return{
            files: null,
        }
    },
    data : vm => ({
        rules : {
          required : {
            required: (v) => !!v || "Required",
  
            minimum : (v) =>  v.length == 10 || " 10 Characters is required",
          }
        },
  
        vehicle : {
          owner_name:'',
          mobile_number:'',
          supplier_type:'',
          vehicle_type:'',
          fuel_type:'',
          vehicle_capacity:'',
          registration_no:'',
          insurance_no:'',
          issue_date:'',
          expiry_date:'',
        },
      }),
    
      methods: {
        async submit(){
          this.$storage.setUniversal('vehicle',this.vehicle.mobile_number)
        let  url = "http://127.0.0.1:8000/vehicle"
        let res= await this.$axios.post(url, this.vehicle)
        console.log(res.data)
        
        if(res.data === true){
          this.$router.push('/corporate_profile')
        }
        else{
          console.error("register failed");
        }
        }

      
    }
  }
  </script>
  
  
  
  
  <style></style>
  