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
                              placeholder="Enter Insurance number"
                              prepend-inner-icon="mdi-account-outline"
                              variant="outlined"
                              :rules="[rules.required]"
                            ></v-text-field>
                        </v-col>
                        
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Issue Date</div>
                            <v-menu
                            ref="menu"
                            v-model="menu1"
                            :close-on-content-click="false"
                            :return-value.sync="date"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                v-model="date"
                                label="Picker in menu"
                       
                                readonly
                                v-bind="attrs"
                                v-on="on"
                              ></v-text-field>
                            </template>
                            <v-date-picker v-model="date" no-title scrollable>
                              <v-spacer></v-spacer>
                              <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                              <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                            </v-date-picker>
                          </v-menu>
                        </v-col>
                        
                        <v-col>
                            <div class="text-subtitle-1 text-medium-emphasis">Expiry Date</div>
                            
                            <v-menu
                              v-model="menu2"
                              :close-on-content-click="false"
                              :nudge-right="40"
                              transition="scale-transition"
                              offset-y
                              min-width="290px"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="date"
                                  label="Picker without buttons"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                ></v-text-field>
                              </template>
                              <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
                            </v-menu>
                        </v-col>
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
          supplier_type:'',
          vehicle_type:'',
          fuel_type:'',
          vehicle_capacity:'',
          registration_no:'',
          insurance_no:'',
          issue_date:'',
          expiry_date:'',
        },

        date: new Date().toISOString().substr(0, 10),
        dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
        menu1: false,
        menu2: false,
      }),
  
      computed: {
        computedDateFormatted () {
          return this.formatDate(this.date)
        },
      },
  
      watch: {
        date (val) {
          this.dateFormatted = this.formatDate(this.date)
        },
      },
      methods: {
        formatDate (date) {
          if (!date) return null
  
          const [year, month, day] = date.split('-')
          return `${month}/${day}/${year}`
        },
        parseDate (date) {
          if (!date) return null
  
          const [month, day, year] = date.split('/')
          return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        },
        async submit(){
          this.$storage.setUniversal('vehicle',this.vehicle.registration_no)
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
  