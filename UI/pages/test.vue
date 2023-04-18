<template>
<v-container>
    <v-row v-for="data in d " :key="data.id">
        {{ data.name }}
    </v-row>
</v-container>


</template>
<script>
export default {
  props: {
  },
    name:"Sajith",
    data :()=>({
        d : [
            {
                id: 1,
                name : "Sajith"
            },
            {
                id: 2,
                name:"sanju"
            }

            
        ]
    })
}
</script>