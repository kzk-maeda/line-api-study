const url = "https://wu4qhqezbd.execute-api.ap-northeast-1.amazonaws.com/dev/callback/"

function bindUrl (path) {
  return url + path
}

var age = {
  name: '年齢',
  value: 20
};

var height = {
  name: '身長',
  value: 150
};

var weight = {
  name: '体重',
  value: 60
};

var vmAge = new Vue({
 el: "#age",
 data: {
   item: age
 }
});

var vmHeight = new Vue({
  el: "#height",
  data: {
    item: height
  }
});

var vmWeight = new Vue({
  el: "#weight",
  data: {
    item: weight
  }
});

var vmPost = new Vue({
  el: "#button",
  data: [
    age,
    height,
    weight
  ],
  mounted() {
    this.postValues('postback')
  },
  methods: {
    postValues(path) {
      var url = bindUrl(path);
      var event = JSON.stringify({
        "type": "process",
        "data": this.data
      })
      axios.post(url, event)
    }
  },
})