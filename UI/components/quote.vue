<template>
  <v-content>
    <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">Create a Quote</h1></v-text-title>
    <br>
     <v-container fluid fill-height>
        <v-layout align-center justify-center>
           <v-flex xs12 sm8 md5>
                    <v-form @submit.prevent="submitForm">
                    <v-row>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Select the vehicle</div>

                        <v-select
                                v-model="quote.Select_the_vehicle"
                                label="Select_the_car"
                                dense outlined prepend-icon="mdi-car"
                              :items="['Renault Kwid', 'Maruti Suzuki WagonR', 'GHyundai Santro', 'Maruti Suzuki Ignis', 'Hyundai Grand i10 Nios', 'Maruti Suzuki Baleno','Ford Figo','Tata Altroz','Maruti Suzuki Dzire','Skoda Rapid','Honda City 4th Gen','Hyundai Venue']"
                              :rules="[v=> !!v ||'select car is required']"
                              ></v-select>
                      </v-col>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Select the Driver</div>

                        <v-select
                                v-model="quote.Select_the_driver"
                                label="Select_the_driver"
                                dense outlined prepend-icon="mdi-car"
                              :items="['Ramesh', 'John', 'Suresh', 'Mahesh', 'Mani kandan']"
                              :rules="[v=> !!v ||'select car is required']"
                              ></v-select>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Waiting Charge</div>

                        <v-text-field 
                        v-model="quote.waiting_charge" 
                        label="waiting_charge" dense outlined prepend-icon="mdi-clock" 
                        :rules="[v => !!v || 'Waiting charge is required']">
                      </v-text-field>
                      </v-col>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Total Cost for Ride</div>

                        <v-text-field v-model="quote.total_amount" 
                        label="total_amount" dense outlined prepend-icon="mdi-cash" 
                        :rules="[v => !!v || 'Total amount is required']">
                      </v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Vehicle number</div>
                        <v-text-field v-model="quote.car_number" 
                        label="car_number" dense outlined prepend-icon="mdi-car" 
                        :rules="[v => !!v || 'Car number is required']">
                      </v-text-field>
                      </v-col>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Driver number</div>
                        <v-text-field v-model="quote.driver_number" 
                        label="car_number" dense outlined prepend-icon="mdi-car" 
                        :rules="[v => !!v || 'Car number is required']">
                      </v-text-field>
                      </v-col>
                    </v-row>
                    <v-row justify="center">
                      <v-btn text @click="submit()">
                        Submit
                      </v-btn>
                    </v-row>      
                   

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
        date: '',
        time: '',
      };
    },
    computed: {
      datetime() {
        if (this.date && this.time) {
          return new Date(`${this.date}T${this.time}`);
        }
        return null;
      },
    },
  };
  </script>
  
  
  
  <script>
  export default {
    layout:'quote_layout',
  }
  </script>
     
     <script>
     export default {
       data(){
         return {
          mobile_number: '',
           Select_the_vehicle:'',
           Select_the_driver:'',
           waiting_charge:'',
           total_amount:'',
           car_number:'',
           driver_number:'',
   
           quote:{
            id:this.$storage.getUniversal('trip_id'),
            mobile_number: this.$storage.getUniversal('trip_number'),
           Select_the_vehicle:'',
           Select_the_driver:'',
           waiting_charge:'',
           total_amount:'',
           car_number:'',
           driver_number:'',
           }
         }
       },
       methods:{
         async submit(){
           this.$storage.setUniversal('user_quote', this.quote.mobile_number)
           this.$storage.setUniversal('driver_quote', this.quote.driver_number)
           let  url = "http://127.0.0.1:8000/quote"
           let res= await this.$axios.post(url, this.quote)
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