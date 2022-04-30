<template>
  <div id="app">
    <h1>Tomada de decisão</h1>
    <hr>
    <DecisionTable tableName="Lucro" :table="tableLucro" />
    <DecisionTable tableName="Investimento" :table="tableInvestimento" />
  </div>
</template>

<script>
import DecisionTable from "./DecisionTable"

export default {
  name: 'App',
  components: {
    DecisionTable
  },
  data() {
    return {
      tableLucro: [
        ['Publicar/Vendas', 1000, 1200, 1400],
        [1000, 3500, 3100, 3700],
        [1200, 2800, 4500, 2900],
        [1400, 2600, 3800, 4950]
      ],
      tableInvestimento: [
        ['Publicar/Vendas', 1000, 1200, 1400],
        [1000, 11500, 14900, 17300],
        [1200, 14200, 13500, 16900],
        [1400, 16400, 16200, 15500]
      ]
    }
  },
}
</script>

<style>
h1 { 
  color: #606060; 
  font-family: 'Trocchi', serif; 
  font-size: 32px; 
  font-weight: normal; 
  line-height: 48px;
  margin: 0; 
}

h3 { 
  color: #606060; 
  font-family: 'Trocchi', serif; 
  font-size: 20px; 
  font-weight: normal; 
  line-height: 48px;
  margin: 0; 
}

</style>