<template>
  <div>
    <v-card class="card">
      <v-card-title>Where to?</v-card-title>
      <v-card-text>
        <v-select
          label="current_location"
          dense outlined prepend-icon="mdi-map"
          :items="['T.Nagar', 'Anna Nagar', 'Guindy', 'Adyar', 'Vepery', 'Saidapet']"
          v-model="trip.current_location"
          :rules="[v => !!v || 'Current location is required']"
        ></v-select>
      </v-card-text>

      <v-card-text>
        <v-select
          label="Select_Your_destination"
          dense outlined prepend-icon="mdi-map-marker"
          :items="['T.Nagar', 'Anna Nagar', 'Guindy', 'Adyar', 'Vepery', 'Saidapet']"
          v-model="trip.Select_Your_destination"
          :rules="[v => !!v || 'Destination is required']"
        ></v-select>
      </v-card-text>
      
      <v-card-text>
        <v-select
          label="Number_of_Seats"
          dense outlined prepend-icon="mdi-car"
          :items="['1', '3', '4', '5', '7']"
          v-model="trip.Number_of_Seats"
          :rules="[v => !!v || 'Number of seats is required']"
        ></v-select>
      </v-card-text>

      <v-card-text>
        <label>Date:</label>
        <input type="date" v-model="trip.date" :rules="[v => !!v || 'Date is required']">
        &ensp; &ensp; &ensp;
        <label>time:</label> 
        <input type="time" v-model="trip.time" :rules="[v => !!v || 'time is required']">
      </v-card-text>

      <v-card-text>
        <v-btn text @click="submit()">
          Submit
        </v-btn>
      </v-card-text>
    </v-card>
  </div>
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
      current_location:'',
      Select_Your_destination:'',
      Number_of_Seats:'',
      date:'',
      time:'',
      trip:{
        current_location:'',
        Select_Your_destination:'',
        Number_of_Seats:'',
        date:'',
        time:'',
      }
    }
  },
  methods:{
    async submit(){
      this.$storage.setUniversal('user_trip',this.trip.Select_Your_destination)
      let  url = "http://127.0.0.1:8000/trip"
      let res= await this.$axios.post(url, this.trip)
      console.log(res.data)
      
      if(res.data === true){
        this.$router.push('/corporate_profile')
      }
      else{
        console.error("trip failed");
      }
    }
  }
}
</script>


<style></style>
