<template>
<v-content>
  <v-text-title><h1 style="text-align: center;" class="font-bold text-3xl">Create a Trip </h1></v-text-title>
  <br>
   <v-container fluid fill-height>
      <v-layout align-center justify-center>
         <v-flex xs12 sm8 md5>
                  <v-form>
               
                    <v-row> <v-col>
                      <div class="text-subtitle-1 text-medium-emphasis">Pickup Location</div>
                      <v-select
                      label="select the pickup location"
                      dense outlined prepend-icon="mdi-map"
                      :items="['T.Nagar', 'Anna Nagar', 'Guindy', 'Adyar', 'Vepery', 'Saidapet']"
                      v-model="trip.current_location"
                      :rules="[v => !!v || 'Current location is required']"
                    ></v-select>
                      </v-col>
                      <v-col>
                        <div class="text-subtitle-1 text-medium-emphasis">Destination</div>
                        <v-select
                          label="Select your destination"
                          dense outlined prepend-icon="mdi-map-marker"
                          :items="['T.Nagar', 'Anna Nagar', 'Guindy', 'Adyar', 'Vepery', 'Saidapet']"
                          v-model="trip.Select_Your_destination"
                          :rules="[v => !!v || 'Destination is required']"
                        ></v-select>
                      </v-col>
                      </v-row>
                      <v-row>
                        <v-col>
                          <div class="text-subtitle-1 text-medium-emphasis">Select Seats</div>
                          <v-select
                            label="Number_of_Seats"
                            dense outlined prepend-icon="mdi-car"
                            :items="['1', '3', '4', '5', '7']"
                            v-model="trip.Number_of_Seats"
                            :rules="[v => !!v || 'Number of seats is required']"
                          ></v-select>
                        </v-col>
                        <v-col>
                          <div class="text-subtitle-1 text-medium-emphasis">Select the car</div>
                          <v-select
                            label="Select the Car"
                            dense outlined prepend-icon="mdi-car"
                            :items="['CAR-SEDAN', 'CAR-SUV', 'CAR-PRIME', 'CAR-MINI','AUTO']"
                            v-model="trip.select_car"
                            :rules="[v => !!v || 'Number of seats is required']"
                          ></v-select>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col>
                          <div class="text-subtitle-1 text-medium-emphasis">Date</div>
                       
                          <input  type="date" v-model="trip.date" :rules="[v => !!v || 'Date is required']">
                        </v-col>
                        <v-col>
                          <div class="text-subtitle-1 text-medium-emphasis">Time</div>
                          <input type="time" v-model="trip.time" :rules="[v => !!v || 'time is required']">
                        </v-col>
                      </v-row>
                      </v-form>
                      <br><br><br>
                      <v-row justify="center">
                        <v-btn text @click="submit()">
                          Submit
                        </v-btn>
                      </v-row>
                      </v-flex>
                      </v-layout>
                      </v-container>
                      </v-content>

</template>


<script>
export default {
  layout: 'Trip_layout',
};
</script>
<script>
export default {
  data(){
    return {
      trip:{
        id:'',
        mobile_number:this.$storage.getUniversal('customer_mobile'),
        
        current_location:'',
        Select_Your_destination:'',
        Number_of_Seats:'',
        select_car:'',
        date:'',
        time:'',
      }
    }
  },
  methods:{
    async mounted(){
      this.trip.mobile = this.$storage.getUniversal('customer_mobile')

      console.log('this.trip.mobile')

    },

    async submit(){
      this.$storage.setUniversal('user_trip',this.trip.id)
      this.$storage.setUniversal('user_trip_mobile',this.trip.mobile_number)
      let  url = "http://127.0.0.1:8000/trip"
      let res= await this.$axios.post(url, this.trip)
      console.log(res.data)
      
      if(res.data === true){
        this.$router.push('/profile_user')
      }
      else{
        console.error("trip failed");
      }
    }
  }
}
</script>


<style></style>
