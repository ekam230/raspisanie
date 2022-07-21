<template>
  {{time}} <br> {{date}}
</template>

<script>
export default {
    data() {
            return {
              interval: null,
              time: null,
              date: null
            }
          },
          beforeDestroy() {
            // prevent memory leak
            clearInterval(this.interval)
          },
          created() {
            // update the time every second
            this.interval = setInterval(() => {
              // Concise way to format time according to system locale.
              // In my case this returns "3:48:00 am"
              this.time = Intl.DateTimeFormat(navigator.language, {
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric'
              }).format();
              this.date = Intl.DateTimeFormat().format()
            }, 1000)
          },
        
    }
</script>

<style>

</style>