<template>
    <v-container>
        <br><br>

      <v-text-title>
        <h1 style="text-align: center;" 
            class="font-bold text-4xl"
        >
           Trip Booking
        </h1>
        <br>
        <br>
        <br>
        
      </v-text-title>
        <v-row justify="center">
            <v-card width="900px">
                
              <v-card-title 
                class="blue darken-1 white--text font-weight-black title"
              >
                PAYMENT<br>
                DETAILS<v-spacer></v-spacer>
          
                <v-img 
                  aspect-ratio="3.075" max-height="40"                              position="right" contain
                />
              </v-card-title>
          
              <v-card-text class='pb-10'>
                <v-row>
                  <v-col cols='6'>
                    <v-subheader class="grey--text text--lighten-1 pl-0 subheader">CARDHOLDER’S NAME</v-subheader>
                    <v-text-field
                    v-model="payment.name"
                        single-line outlined label="Name" hide-details
                    />
                  </v-col>
          
                  <v-col cols='6'>
                    <v-subheader class="grey--text text--lighten-1 pl-0 subheader">CARD NUMBER</v-subheader>
                    <v-text-field
                    v-model="payment.card_number"
                        single-line outlined mask="credit-card" label="XXXX XXXX XXXX XXXX"  hide-details
                    />
                  </v-col>
          
                  <v-col col='4'>
                    <v-subheader class="grey--text text--lighten-1 pl-0 subheader">EXPIRY DATE</v-subheader>           
                    <v-select
                      :items="MonthList" label="Month" outlined
                      v-model="payment.exp_month"
                     hide-details
                    />
                  </v-col>
          
                  <v-col col='4'>
                    <v-subheader class="grey--text text--lighten-1 pl-0 subheader"></v-subheader>                   
                    <v-select
                      :items="YearList" label="Year" outlined
                      v-model="payment.exp_date"
                      hide-details
                    />
                  </v-col>
          
                  <v-col col='4'>
                    <v-subheader class="grey--text text--lighten-1 pl-0 subheader">CVV</v-subheader>             
                    <v-text-field
                    v-model="payment.cvv"
                     single-line outlined hide-details/>  
                  </v-col>
          
                </v-row>
                    </v-card-text>

                    
            <v-form>
                <v-row justify="center">
                    <v-btn   color="black darken-3"   text @click="submit()">Submit</v-btn>
                </v-row>
        </v-form>
          <br>
                </v-card>
            </v-row>
       
      
    </v-container>
</template>

<script>
export default{
    name: 'booking',
    data () {
 
    this.YearList =  ['2030','2029','2028','2017','whatever'];    
    this.MonthList =  ["January", "February", "March", "April", "May", "June", "Jully", "August", "September", "October", "November", "December"
];           
    return {
        name: '',
    card_number: '',
    exp_month: '',
    exp_date: '',
    cvv: '',

    payment:{
        mobile_number: this.$storage.getUniversal('trip_number'),
        name: '',
    card_number: '',
    exp_month: '',
    exp_date: '',
    cvv: '',
    }
    }
  },
  methods:{
    async submit(){

          this.$storage.setUniversal('payment',this.payment.mobile_number)
        let  url = "http://127.0.0.1:8000/payment"
        let res= await this.$axios.post(url, this.payment)
        console.log(res.data)
        
        
        if(res.data === true){
          this.$router.push('/profile_user')
          console.log("payment is successfully done")
        }
        else{
          console.error("register failed");
        }
    },
    async close(){
        this.$router.push('/profile_user')
    }
}
}


</script>