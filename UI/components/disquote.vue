<template>


  <v-container fluid>
    <br><br>

    <v-text-title>
      <h1 style="text-align: center;" 
          class="font-bold text-4xl"
      >
         User Requests
      </h1>
    </v-text-title>

    <br><br>

    <v-row
    
    v-for="trip in trip_data"
    :key="trip.mobile_number"
    >
        <v-list>
          <v-card width="1750px">
            <v-row>
              <v-col>
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>
                      mdi-map-marker
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>{{ trip.current_location }}</v-list-item-title>
                    <v-list-item-subtitle>Pickup Point</v-list-item-subtitle>
                  </v-list-item-content>  
                </v-list-item>
              </v-col>
              <v-col>
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>
                      mdi-map-marker-check
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>{{ trip.Select_Your_destination }}</v-list-item-title>
                    <v-list-item-subtitle>Destination Point</v-list-item-subtitle>
                  </v-list-item-content>  
                </v-list-item>
              </v-col>
              <v-col>
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>
                      mdi-calendar
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>{{ trip.date }}</v-list-item-title>
                    <v-list-item-subtitle>Date</v-list-item-subtitle>
                  </v-list-item-content>  
                </v-list-item>
              </v-col>
              <v-col>
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>
                      mdi-clock
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>{{ trip.time }}</v-list-item-title>
                    <v-list-item-subtitle>Time</v-list-item-subtitle>
                  </v-list-item-content>  
                </v-list-item>
              </v-col>
              <v-col style="padding-top: 1.3%;">
                <v-btn icon style="margin-right: 5%;" color="success" @click="ride()" >
                  <v-icon>
                    mdi-check
                  </v-icon>
                
              </v-btn>
              <v-btn icon color="error" @click="del()">
                <v-icon>
                  mdi-delete
                </v-icon>
              
            </v-btn>
              </v-col>

            </v-row>

            
          </v-card>
        </v-list>
    </v-row>
  </v-container>

</template>
<script>
export default {
  async mounted(){
      this.$vuetify.theme.dark = false;
      this.trip = this.$storage.getUniversal('user_trip')
      let url = "http://127.0.0.1:8000/trip/all"
      let res = await this.$axios.get(url,{params:{id: this.trip}})
      this.trip_data = res.data
      console.log(this.trip_data)

  },
  data: () =>({
      trip:"",
      mobile_number:"",
      trip_data:[],  
  })
}

</script>