<template>


      <v-container fluid>
        <br><br>

        <v-text-title><h1 style="text-align: center;" class="font-bold text-4xl">Quotes</h1></v-text-title>
        <br><br>
        <v-row justify="center">
            <v-card
            width="50%"
            >
            <v-img
            src="https://ssranatourandtravels.com/assets/images/2.jpg"
            class="align-end"
          
            height="300px"
            cover
          ></v-img>
            <v-row>
                <v-col>
                    <v-list-item>
                        <v-list-item-icon>
                          <v-icon>
                            mdi-account
                          </v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>       </v-list-item-title>
                          <v-list-item-subtitle>Agency Name</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                <v-col>
                    <v-list-item>
                        <v-list-item-icon>
                            <v-icon>
                              mdi-car
                            </v-icon>
                          </v-list-item-icon>  
                          <v-list-item-content>
                            <v-list-item-title> </v-list-item-title>
                            <v-list-item-subtitle>Vehicle Type</v-list-item-subtitle>
                          </v-list-item-content>
                    </v-list-item>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-list-item>
                        <v-list-item-icon>
                            <v-icon>
                              mdi-car
                            </v-icon>
                          </v-list-item-icon>
                          
                          <v-list-item-content>
                            <v-list-item-title>   </v-list-item-title>
                            <v-list-item-subtitle>Vehicle Number</v-list-item-subtitle>
                          </v-list-item-content>
              
                    </v-list-item>
                </v-col>
                <v-col>
                                
                <v-list-item>
                    <v-list-item-icon>
                      <v-icon>
                        mdi-account
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>  </v-list-item-title>
                      <v-list-item-subtitle>Driver Name</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                </v-col>
            </v-row> 
            <v-row>
                <v-col>
                    <v-list-item>
                        <v-list-item-icon>
                          <v-icon>
                            mdi-cash
                          </v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>  </v-list-item-title>
                          <v-list-item-subtitle>Waiting Charge</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                <v-col>
                    <v-list-item>
                        <v-list-item-icon>
                          <v-icon>
                            mdi-cash
                          </v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>  </v-list-item-title>
                          <v-list-item-subtitle>Total Fare</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
            </v-row>
            <br>
    
              <v-card-actions>            
                <v-row justify="center">
                    <v-spacer></v-spacer>
                    <v-col>
                        <v-btn color="black" text>
                            Accept
                          </v-btn>
                          <v-btn color="black" text>
                            Delete
                          </v-btn>
                    </v-col>
                    <v-spacer></v-spacer>


                </v-row>
                
              </v-card-actions>
            </v-card>
        </v-row>
      </v-container>
   
  </template>