<template>
    <div>
        <div class="shadow p-3 mb-5 bg-white rounded" v-for="(item, index) in items" :key="index">
            <div class="form-group">
                <label for="exampleInputEmail1">업무내용</label>
                <textarea class="form-control w-75" rows="5" id="comment" v-model="item.txt"></textarea>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'shadow-box',
  props: ['items']
}
</script>

<style scoped>
</style>

