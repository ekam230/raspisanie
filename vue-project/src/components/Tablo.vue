<template>
<div class="columns is-size-5">            
    <div class="column is-2">
        {{myObject.operator}}
    </div>
    <div class="column is-1 has-text-centered">              
        {{myObject.time}}
    </div>
    <div class="column is-2">
        {{myObject.path}}
    </div>
    <div class="column is-3">
        {{myObject.name}}
    </div>
    <div class="column is-2">
        {{myObject.terminal}}
        </div>
    <div class="column is-2">
        {{myObject.remarks}}
    </div>
</div>
</template>

<script>
export default {
    props: ['myObject']
    // props: ['name','time','operator','path','terminal','remarks']
}
</script>

<style>

</style>