<template>
    <div class="info-section">
        <div class="info-header">
            <div class="image-wrap">
                <img :src="profileImage" alt="Profile Image" v-if="profileImage" />
            </div>

            <hr>

            <div class="main-info">
                <h1>{{ username }}</h1>

                <div>
                    <p>Followers: {{ followers }}</p>
                    <button>Follow</button>
                </div>

                <hr>


                <div>
                    <p>{{ age }} years old</p>
                    <p>Gender - {{ gender }}</p>
                </div>
            </div>

            <hr>
        </div>

        <div class="bio">
            <p>{{ bio }}</p>
        </div>

        <div class="info-footer">
        </div>
    </div>
</template>

<script>
export default {
    props: ['profileImage', 'username', 'age', 'gender', 'bio', 'followers']
}
</script>

<style>
@import "@/assets/styles/profile.scss";
</style>