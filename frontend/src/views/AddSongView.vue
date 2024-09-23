<template>
    <div class="container">
        <form v-on:submit.prevent="addSong">
            <div class="form-title">
                <h3>Add song</h3>
            </div>

            <div class="input-block">
                <label for="name">Name</label>
                <input type="text" id="name">
            </div>

            <div class="input-block buttons">
                <label for="song">song</label>
                <label for="thumbnail">image</label>

                <input type="file" id="thumbnail">
                <input type="file" id="song">
            </div>
        </form>
    </div>
</template>

<script>
export default {}
</script>

<style lang="scss">
@import "@/assets/styles/authentication.scss";

.input-block {
    &.buttons {

    }

    input[type="file"] {
        display: none;
    }
}
</style>