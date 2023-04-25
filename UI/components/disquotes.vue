<template>


    <v-container fluid>
      <br><br>
  
      <v-text-title>
        <h1 style="text-align: center;" 
            class="font-bold text-4xl"
        >
           User Quotes
        </h1>
      </v-text-title>
  
      <br><br>
  
      <v-row
      
      v-for="quote in quote_data"
      :key="quote.mobile_number"
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
                      <v-list-item-title>{{ quote.Select_the_vehicle }}</v-list-item-title>
                      <v-list-item-subtitle>Assigned Vehicle</v-list-item-subtitle>
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
                      <v-list-item-title>{{ quote.Select_the_driver }}</v-list-item-title>
                      <v-list-item-subtitle>Driver Name</v-list-item-subtitle>
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
                      <v-list-item-title>{{ quote.driver_number}}</v-list-item-title>
                      <v-list-item-subtitle>Driver Number</v-list-item-subtitle>
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
                      <v-list-item-title>{{ quote.waiting_charge }}</v-list-item-title>
                      <v-list-item-subtitle>Waiting Charge</v-list-item-subtitle>
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
                      <v-list-item-title>{{ quote.total_amount }}</v-list-item-title>
                      <v-list-item-subtitle>Total amount</v-list-item-subtitle>
                    </v-list-item-content>  
                  </v-list-item>
                </v-col>
                <v-col style="padding-top: 1.3%;">
                  <v-btn icon style="margin-right: 5%;" color="success" @click="ride(quote.mobile_number, quote.driver_number)" >
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
        this.quote = this.$storage.getUniversal('trip_number')
        console.log(this.quote)
             
        let url = "http://127.0.0.1:8000/quote/user/all"
        let res = await this.$axios.get(url,{params:{mobile_number: this.quote}})
        this.quote_data = res.data
        
  
    },
    data: () =>({
        quote:"",
        mobile_number:"",
        quote_data:[],  
    }),
    methods: {
      async ride(mobile_number, driver_number){
        console.log(mobile_number, driver_number)
        this.$router.push('/user_book')
      }
    }
  }
  
  </script>