<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="a">a:</label>
      <input type="text" id="a" v-model="formData.a" required>

      <label for="b">b:</label>
      <input type="text" id="b" v-model="formData.b" required>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        a: '',
        b: '',
      },
    };
  },
  methods: {
    submitForm() {
      // 使用 Axios 發送 POST 請求到 Flask 服務器
      axios.post('http://127.0.0.1:5001/a', this.formData)
        .then(response => {
          // 在這裡處理服務器的回應
          console.log(response.data);
        })
        .catch(error => {
          // 在這裡處理錯誤
          console.error(error);
        });
    },
  },
};
</script>

<style>
/* 添加樣式，可選 */
</style>