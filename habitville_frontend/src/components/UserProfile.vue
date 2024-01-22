<template>
    <div class="profile-container">
      <h1>User Profile</h1>
      <form @submit.prevent="updateProfile">
        <div class="form-group">
          <label for="username">Username:</label>
          <input id="username" v-model="user.username" type="text" required />
        </div>
        <div class="form-group">
          <label for="goals">Goals:</label>
          <textarea id="goals" v-model="user.goals" placeholder="Write your goals/motivations here!"></textarea>
        </div>
        <button type="submit">Update Profile</button>
      </form>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserProfile',
    data() {
      return {
        user: {
          username: '',
          goals: '',
        }
      };
    },
    created() {
      this.loadUserProfile();
    },
    methods: {
      async loadUserProfile() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/accounts/profile/', { withCredentials: true });
          this.user = response.data;
        } catch (error) {
          console.error('Error loading user profile:', error);
        }
      },
      async updateProfile() {
        try {
          const response = await axios.put('http://127.0.0.1:8000/accounts/profile/', this.user, { withCredentials: true });
          console.log('Profile updated:', response.data);
          alert('Profile updated successfully');
        } catch (error) {
          console.error('Error updating profile:', error);
        }
      }
    }
  };
  </script>
  
  
  <style scoped>
  .profile-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
  }
  
  .form-group input, .form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 15px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #4cae4c;
  }
  
  .error-message {
    color: red;
    text-align: center;
  }
  </style>
  