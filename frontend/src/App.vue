<template>
  <div id="app">
    <h2>Lista 01</h2>
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