
$(document).ready(function () {
    $('#example').DataTable();
});

$(document).ready(function () {
    $('#example2').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'pdf'
        ]
    });
});



$(document).ready(function () {
  $('#example3').DataTable({
    dom: 'Bfrtip',
    buttons: [
      'excel'
    ]
  });
});
