<template>
  <div class="huangli-container">
    <van-cell-group inset>
      <van-cell>
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" fill="currentColor"/>
              <path d="M686.7 638.6L544.1 535.5V288c0-4.4-3.6-8-8-8H488c-4.4 0-8 3.6-8 8v275.4c0 2.6 1.2 5 3.3 6.5l165.4 120.6c3.6 2.6 8.6 1.8 11.2-1.7l28.6-39c2.6-3.7 1.8-8.7-1.8-11.2z" fill="currentColor"/>
            </svg>
            <span>阳历</span>
          </div>
        </template>
        <template #value>{{ data.yangli }}</template>
      </van-cell>

      <van-cell>
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64c247.4 0 448 200.6 448 448S759.4 960 512 960 64 759.4 64 512 264.6 64 512 64zm0 76.8C307.2 140.8 140.8 307.2 140.8 512S307.2 883.2 512 883.2 883.2 716.8 883.2 512 716.8 140.8 512 140.8z" fill="currentColor"/>
              <path d="M512 512m-179.2 0a179.2 179.2 0 1 0 358.4 0 179.2 179.2 0 1 0-358.4 0Z" fill="currentColor"/>
            </svg>
            <span>阴历</span>
          </div>
        </template>
        <template #value>{{ data.yinli }}</template>
      </van-cell>

      <van-cell>
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32zM368 744c0 4.4-3.6 8-8 8h-80c-4.4 0-8-3.6-8-8V280c0-4.4 3.6-8 8-8h80c4.4 0 8 3.6 8 8v464zm384 0c0 4.4-3.6 8-8 8h-80c-4.4 0-8-3.6-8-8V280c0-4.4 3.6-8 8-8h80c4.4 0 8 3.6 8 8v464z" fill="currentColor"/>
            </svg>
            <span>五行</span>
          </div>
        </template>
        <template #value>{{ data.wuxing }}</template>
      </van-cell>

      <van-cell>
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64L128 448l128 128 256-256 256 256 128-128L512 64zM256 640v192h512V640H256z" fill="currentColor"/>
            </svg>
            <span>冲煞</span>
          </div>
        </template>
        <template #value>{{ data.chongsha }}</template>
      </van-cell>

      <van-cell class="multi-line">
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M880 184H712v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H384v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H144c-17.7 0-32 14.3-32 32v664c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V216c0-17.7-14.3-32-32-32z" fill="currentColor"/>
            </svg>
            <span>彭祖百忌</span>
          </div>
        </template>
        <template #value>{{ data.baiji }}</template>
      </van-cell>

      <van-cell class="multi-line">
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm193.5 301.7l-210.6 292a31.8 31.8 0 0 1-51.7 0L318.5 484.9c-3.8-5.3 0-12.7 6.5-12.7h46.9c10.2 0 19.9 4.9 25.9 13.3l71.2 98.8 157.2-218c6-8.3 15.6-13.3 25.9-13.3H699c6.5 0 10.3 7.4 6.5 12.7z" fill="currentColor"/>
            </svg>
            <span>吉神宜趋</span>
          </div>
        </template>
        <template #value>{{ data.jishen }}</template>
      </van-cell>

      <van-cell class="highlight good">
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm193.5 301.7l-210.6 292a31.8 31.8 0 0 1-51.7 0L318.5 484.9c-3.8-5.3 0-12.7 6.5-12.7h46.9c10.2 0 19.9 4.9 25.9 13.3l71.2 98.8 157.2-218c6-8.3 15.6-13.3 25.9-13.3H699c6.5 0 10.3 7.4 6.5 12.7z" fill="currentColor"/>
            </svg>
            <span>宜</span>
          </div>
        </template>
        <template #value>{{ data.yi }}</template>
      </van-cell>

      <van-cell class="multi-line">
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm165.4 618.2l-66-.3L512 563.4l-99.3 118.4-66.1.3c-4.4 0-8-3.5-8-8 0-1.9.7-3.7 1.9-5.2l130.1-155L340.5 359a8.32 8.32 0 0 1-1.9-5.2c0-4.4 3.6-8 8-8l66.1.3L512 464.6l99.3-118.4 66-.3c4.4 0 8 3.5 8 8 0 1.9-.7 3.7-1.9 5.2L553.5 514l130 155c1.2 1.5 1.9 3.3 1.9 5.2 0 4.4-3.6 8-8 8z" fill="currentColor"/>
            </svg>
            <span>凶神宜忌</span>
          </div>
        </template>
        <template #value>{{ data.xiongshen }}</template>
      </van-cell>

      <van-cell class="highlight bad">
        <template #title>
          <div class="cell-title">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64zm165.4 618.2l-66-.3L512 563.4l-99.3 118.4-66.1.3c-4.4 0-8-3.5-8-8 0-1.9.7-3.7 1.9-5.2l130.1-155L340.5 359a8.32 8.32 0 0 1-1.9-5.2c0-4.4 3.6-8 8-8l66.1.3L512 464.6l99.3-118.4 66-.3c4.4 0 8 3.5 8 8 0 1.9-.7 3.7-1.9 5.2L553.5 514l130 155c1.2 1.5 1.9 3.3 1.9 5.2 0 4.4-3.6 8-8 8z" fill="currentColor"/>
            </svg>
            <span>忌</span>
          </div>
        </template>
        <template #value>{{ data.ji }}</template>
      </van-cell>
    </van-cell-group>
  </div>
</template>

<script setup>
defineProps({
  data: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.huangli-container {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.12);
}

.cell-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon {
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}

.cell-title:hover .icon {
  transform: scale(1.1);
}

:deep(.van-cell) {
  padding: 16px;
}

:deep(.multi-line .van-cell__value) {
  white-space: pre-wrap;
  line-height: 1.5;
}

:deep(.highlight .van-cell__title) {
  font-weight: bold;
}

:deep(.good) {
  background: rgba(82, 196, 26, 0.08);
}

:deep(.good .van-cell__value) {
  color: #52c41a;
}

:deep(.bad) {
  background: rgba(255, 77, 79, 0.08);
}

:deep(.bad .van-cell__value) {
  color: #ff4d4f;
}

:deep(.good .icon) {
  color: #52c41a;
}

:deep(.bad .icon) {
  color: #ff4d4f;
}

:deep(.van-cell:nth-child(1) .icon) {
  color: #1890ff;
}

:deep(.van-cell:nth-child(2) .icon) {
  color: #722ed1;
}

:deep(.van-cell:nth-child(3) .icon) {
  color: #eb2f96;
}

:deep(.van-cell:nth-child(4) .icon) {
  color: #fa8c16;
}

:deep(.van-cell:nth-child(5) .icon) {
  color: #13c2c2;
}

:deep(.van-cell:nth-child(6) .icon) {
  color: #52c41a;
}

:deep(.van-cell:nth-child(7) .icon) {
  color: #52c41a;
}

:deep(.van-cell:nth-child(8) .icon) {
  color: #faad14;
}

:deep(.van-cell:nth-child(9) .icon) {
  color: #ff4d4f;
}
</style> 