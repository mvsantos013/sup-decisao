<template>
    <div>
        <h3>{{tableName}}</h3>

        <div style="display: flex;">
            <div style="min-width:300px">
                <table>
                    <tbody>
                    <tr v-for="row, i in table" :key="i">
                        <td v-for="cell, j in row" :key="j">{{cell}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <div style="display: flex; flex-direction: column; padding-left: 10px">
                <button>Dominância</button>
                <button @click="computeMaximax">Maximax</button>
                <button>Maxmin</button>
                <button>Minimax Regret</button>
                <button>Média</button>
            </div>
            <div v-if="result" style="padding-left: 20px">Resultado: {{result}}</div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

const API_PATH = 'https://zf5sqqpile.execute-api.us-east-1.amazonaws.com/dev'
// const API_PATH = 'http://localhost:3000/dev'

export default {
  name: 'App',
  props: {
      table: {
          type: Array,
          default: () => []
      },
      tableName: {
          type: String,
          default: null
      }
  },
  data() {
    return {
        result: null
    }
  },
  methods: {
      async computeDominancia(){
          const response = await axios.post(`${API_PATH}/dominancia`)
          console.log(response)
      },
      async computeMaximax(){
          const response = await axios.post(`${API_PATH}/maximax`, {table: this.table})
          console.log(response)
          this.result = response.data.result
      },
      async computeMaximin(){
          const response = await axios.post(`${API_PATH}/maximin`)
          console.log(response)
      },
      async computeMinimaxRegret(){
          const response = await axios.post(`${API_PATH}/minimax-regret`)
          console.log(response)
      },
      async computeMedia(){
          const response = await axios.post(`${API_PATH}/media`)
          console.log(response)
      }
  }
}
</script>

<style>
table td {
  padding: 5px;
}

table td:first-child, tr:first-child {
  background-color: #ededed;
}
</style>