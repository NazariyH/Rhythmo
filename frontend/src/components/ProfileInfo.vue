<template>
    <div id="info-section" class="info-section active">
        <div class="info-header">
            <div class="image-wrap">
                <img :src="profileImage" alt="Profile Image" v-if="profileImage" />
            </div>

            <hr>

            <div class="main-info">
                <div>
                    <h1>{{ username }}</h1>
                    <router-link :to="{ name: 'profile-edit' }">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-pencil-fill" viewBox="0 0 16 16">
                            <path
                                d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.5.5 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11z" />
                        </svg>
                    </router-link>
                </div>

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

        <div class="bio" v-if="bio">
            <p>{{ bio }}</p>
        </div>

        <div class="info-footer">
        </div>
    </div>
</template>

<script>
export default {
    props: ['profileImage', 'username', 'age', 'gender', 'bio', 'followers'],
    mounted() {
        const infoPannel = document.getElementById('info-section');
        setInterval(() => {
            infoPannel.classList.remove('active');
        }, 100)
    }
}
</script>

<style>
@import "@/assets/styles/profile.scss";
</style>