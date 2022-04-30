<template>
    <div style="margin-bottom: 10px">
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
                <button @click="computeDominancia">Dominância</button>
                <button @click="computeMaximax">Maximax</button>
                <button @click="computeMaximin">Maxmin</button>
                <button @click="computeMinimaxRegret">Minimax Regret</button>
                <button @click="computeMedia">Média</button>
            </div>
            <div style="padding-left: 20px">
                <div v-if="loading">Calculando...</div>
                <div v-if="result">Resultado: {{result}}</div>
                <div v-if="error">{{error}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

// const API_PATH = 'https://zf5sqqpile.execute-api.us-east-1.amazonaws.com/dev'
const API_PATH = 'http://localhost:3000/dev'

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
        result: null,
        error: null,
        loading: false,
    }
  },
  methods: {
      async computeDominancia(){
        this.result = null
        this.error = null
        this.loading = true
        try{
            const response = await axios.post(`${API_PATH}/dominancia`, {table: this.table})
            this.result = response.data.result
            if(!this.result) this.result = 'Não há resultado.'
        }
        catch(e){
            this.error = 'Error: ' + e.response.data.error
        }
        this.loading = false
      },
      async computeMaximax(){
        this.result = null
        this.error = null
        this.loading = true
        try{
            const response = await axios.post(`${API_PATH}/maximax`, {table: this.table})
            this.result = response.data.result
            if(!this.result) this.result = 'Não há resultado.'
        }
        catch(e){
            this.error = 'Error: ' + e.response.data.error
        }
        this.loading = false
      },
      async computeMaximin(){
        this.result = null
        this.error = null
        this.loading = true
        try{
            const response = await axios.post(`${API_PATH}/maximin`, {table: this.table})
            this.result = response.data.result
            if(!this.result) this.result = 'Não há resultado.'
        }
        catch(e){
            this.error = 'Error: ' + e.response.data.error
        }
        this.loading = false
      },
      async computeMinimaxRegret(){
        this.result = null
        this.error = null
        this.loading = true
        try{
            const response = await axios.post(`${API_PATH}/minimax-regret`, {table: this.table})
            this.result = response.data.result
            if(!this.result) this.result = 'Não há resultado.'
        }
        catch(e){
            this.error = 'Error: ' + e.response.data.error
        }
        this.loading = false
      },
      async computeMedia(){
        this.result = null
        this.error = null
        this.loading = true
        try{
            const response = await axios.post(`${API_PATH}/media`, {table: this.table})
            this.result = response.data.result
            if(!this.result) this.result = 'Não há resultado.'
        }
        catch(e){
            this.error = 'Error: ' + e.response.data.error
        }
        this.loading = false
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