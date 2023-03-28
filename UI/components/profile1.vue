<template>
    <v-container>
    <v-card flat
        max-width="775"
        class="mx-auto">
    <v-card-text>
      <h1><b>My info</b></h1>   
                  <br>
  <!--             profile image          -->
  <v-card class="mx-auto" max-width="1000" tile>
    <v-img height="200" src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"></v-img>
    <v-row style="margin:2.5%;position:absolute; top: 130px">
                <v-list-item>
                 <v-list-item-avatar size="100">
                    <img
                      src="https://www.w3schools.com/howto/img_avatar.png"
                      alt="John"
                    >
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title class="title" style="margin-top:40px;">{{ pdata.first_name}} {{ pdata.last_name }}</v-list-item-title>
                    <v-list-item-subtitle>HI HELLO | User</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
  </v-row>
  </v-card>
  <br><br><br><br>
    
        <v-list two-line>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-account
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{pdata.first_name}}</v-list-item-title>
              <v-list-item-subtitle>First Name</v-list-item-subtitle>
              
              
            </v-list-item-content>

            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-account
              </v-icon>
            </v-list-item-icon>
            &ensp;&ensp;
            <v-list-item-content>
              <v-list-item-title>{{pdata.last_name}}</v-list-item-title>
              <v-list-item-subtitle>Last Name</v-list-item-subtitle>
              
              
            </v-list-item-content>
          </v-list-item>
          <v-divider inset></v-divider>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-phone
              </v-icon>
            </v-list-item-icon>
    
            <v-list-item-content>
              <v-list-item-title>{{ pdata.mobile_number }}</v-list-item-title>
              <v-list-item-subtitle>Mobile</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-account-circle
              </v-icon>
            </v-list-item-icon>
            &ensp;&ensp;
    
            <v-list-item-content>
              <v-list-item-title>{{ pdata.aadhar_id }}</v-list-item-title>
              <v-list-item-subtitle>Aadhar ID</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-divider inset></v-divider>
    
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-map
              </v-icon>
            </v-list-item-icon>
    
            <v-list-item-content>
              <v-list-item-title>{{ pdata.location }}</v-list-item-title>
              <v-list-item-subtitle>Location</v-list-item-subtitle>
            </v-list-item-content>
            
          </v-list-item>
          <br>
        </v-list>
            <v-row
              align="center"
              justify="space-around"
            >
            <!--<v-btn
            tile click
            color="success"
            >
            <v-icon left>
              mdi-pencil
            </v-icon>
            Edit
            </v-btn> -->
            <v-btn @click="greet()"
              depressed
              color="error">
              Delete
            </v-btn>               
            </v-row>
                  
        </v-card-text>
      </v-card>
    </v-container>
    </template>

    <script>
  export default {
    name: 'profile1',
    data() {
      return {
        greet: function() {
          alert('Hello!');
        }
      }
    },
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.mobile_number = this.$storage.getUniversal('customer_mobile')
        let url = "http://127.0.0.1:8000/customer"
        console.log(this.mobile_number)
        let res = await this.$axios.get(url,{params:{ mobile_number :this.mobile_number}});
        this.pdata=res.data
        console.log(this.pdata)
    },
    data: () =>({
        mobile_number:"",
        pdata :{},
    }),
  }
  </script>
  
    