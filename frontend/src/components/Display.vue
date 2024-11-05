<template>
  <div class="d-display">
    <h1>Counter: {{ counter }}</h1>
    <button @click="resetCounter">Reset Counter</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      counter: 0,
      intervalId: null
    }
  },
  methods: {
    fetchCounter() {
      axios
        .get('http://localhost:5000/get_counter')
        .then((response) => {
          this.counter = response.data.counter
        })
        .catch((error) => {
          console.error('There was an error fetching the counter:', error)
        })
    },
    resetCounter() {
      axios
        .post('http://localhost:5000/reset_counter')
        .then((response) => {
          console.log(response.data.status)
          this.fetchCounter() // Update counter after reset
        })
        .catch((error) => {
          console.error('There was an error resetting the counter:', error)
        })
    }
  },
  mounted() {
    this.fetchCounter()
    this.intervalId = setInterval(this.fetchCounter, 1000) // Fetch counter every second
  },
  beforeUnmount() {
    clearInterval(this.intervalId) // Clear the interval when the component is destroyed
  }
}
</script>

<style scoped>
.display {
  text-align: center;
  margin-top: 50px;
}
button {
  margin-top: 20px;
}
</style>
