<template>
  <div class="container">
    <div class="calendar-wrapper">
      <img src="./assets/calendar.svg" alt="日历" class="calendar-icon">
      <h1>老黄历查询</h1>
      
      <!-- 日期显示区域 -->
      <div class="date-display" @click="showCalendar = true">
        <div class="current-date">
          <span class="year">{{ currentYear }}年</span>
          <span class="month">{{ currentMonth }}月</span>
          <span class="day">{{ currentDay }}日</span>
        </div>
        <div class="lunar-date" v-if="huangliData">
          {{ huangliData.yinli }}
        </div>
      </div>

      <!-- 日历控件 -->
      <van-calendar 
        v-model:show="showCalendar"
        @confirm="onConfirm"
        :min-date="minDate"
        :max-date="maxDate"
        color="#1296db"
        :formatter="formatter"
      />
    </div>

    <div v-if="loading" class="loading-wrapper">
      <van-loading type="spinner" color="#1296db" />
      <p>加载中...</p>
    </div>

    <huangli-display 
      v-else-if="huangliData" 
      :data="huangliData"
    />

    <div v-else-if="error" class="error-message">
      {{ error }}
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import dayjs from 'dayjs'
import HuangliDisplay from './components/HuangliDisplay.vue'
import { showToast } from 'vant'

const showCalendar = ref(false)
const selectedDate = ref(dayjs().format('YYYY-MM-DD'))
const huangliData = ref(null)
const loading = ref(false)
const error = ref('')

// 计算当前显示的年月日
const currentYear = computed(() => dayjs(selectedDate.value).year())
const currentMonth = computed(() => dayjs(selectedDate.value).month() + 1)
const currentDay = computed(() => dayjs(selectedDate.value).date())

// 设置日期范围
const minDate = new Date(2010, 0, 1)
const maxDate = new Date(2025, 11, 31)

// 日历自定义样式
const formatter = (day) => {
  const date = dayjs(day.date)
  const isToday = date.format('YYYY-MM-DD') === dayjs().format('YYYY-MM-DD')
  
  if (isToday) {
    day.topInfo = '今天'
    day.className = 'today'
  }
  return day
}

// 缓存数据
const cache = new Map()

// 防抖函数
let timer = null
const fetchData = async (date) => {
  if (timer) clearTimeout(timer)
  
  timer = setTimeout(async () => {
    if (cache.has(date)) {
      huangliData.value = cache.get(date)
      return
    }

    loading.value = true
    error.value = ''
    
    try {
      const response = await axios.get(`http://localhost:8000/huangli/${date}`)
      if (response.data.code === 0) {
        huangliData.value = response.data.data
        cache.set(date, response.data.data)
      } else {
        throw new Error('数据获取失败')
      }
    } catch (err) {
      error.value = '数据获取失败，请稍后重试'
      showToast('数据获取失败，请稍后重试')
    } finally {
      loading.value = false
    }
  }, 300)
}

const onConfirm = (date) => {
  showCalendar.value = false
  const formatDate = dayjs(date).format('YYYY-MM-DD')
  selectedDate.value = formatDate
  fetchData(formatDate)
}

onMounted(() => {
  fetchData(selectedDate.value)
})
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background: rgb(46, 211, 214);
  min-height: 100vh;
}

.calendar-wrapper {
  text-align: center;
  margin-bottom: 20px;
  background: rgba(255, 255, 255, 0.95);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
}

.calendar-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 10px;
}

.date-display {
  margin: 20px 0;
  padding: 20px;
  background: rgba(41, 190, 193, 0.95);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.date-display:hover {
  background: rgba(37, 171, 174, 0.95);
  transform: translateY(-2px);
}

.current-date {
  font-size: 28px;
  color: #ffffff;
  margin-bottom: 10px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.year, .month, .day {
  margin: 0 5px;
}

.lunar-date {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9);
}

.loading-wrapper {
  text-align: center;
  padding: 40px 0;
}

.error-message {
  text-align: center;
  color: #ff4d4f;
  padding: 20px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
}

h1 {
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
}

:deep(.van-calendar__day) {
  margin-bottom: 5px;
}

:deep(.today) {
  background: rgba(46, 211, 214, 0.15);
  border-radius: 4px;
}

:deep(.van-calendar__top-info) {
  font-size: 12px;
  color: rgb(46, 211, 214);
}
</style> 