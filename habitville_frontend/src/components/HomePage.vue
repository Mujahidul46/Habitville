<template>
    <div class="home-container">
        <h1>Welcome to Habitville</h1>
        <p>Habitville is a gamified habit tracker designed specifically for university students. We understand the struggle of maintaining positive habits, managing time effectively, and dealing with stress. That's where Habitville comes in, transforming your daily routines into exciting adventures!</p>

        <h2>Gamify Your Life</h2>
        <p>Immerse yourself in the Habitville world where your progress brings life to a virtual village. Complete habits to play minigames, earn resources, and upgrade your own virtual village!</p>

        <h2>Engaging Minigames</h2>
        <p>Dive into a variety of minigames, such as our relaxing fishing game! Take a well-deserved break by casting your line and reeling in rewards for your village.</p>

        <h2>Organise Your Life</h2>
        <p>Set up daily and recurring habits easily as well as one-off tasks. Track your progress with detailed statistics to see how you're improving over time.</p>
    </div>
</template>
 
<script>
    export default {
        name: 'HomePage'
    };
</script>

<style scoped>
.home-container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    text-align: center;
    font-size: 1.08em;
}

h1 {
    font-size: 2.16em;
}

h2 {
    margin-top: 20px;
    font-size: 1.62em;
}

p {
    font-size: 1.08em;
    line-height: 1.6;
}
</style>

