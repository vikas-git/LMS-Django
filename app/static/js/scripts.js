$(function () {
    // $('.alert').addClass('in');
    // if (app.config.get('autoremove_flash', true)) {
    //     $('.alert.alert-info, .alert.alert-success').autoremove(10);
    // }

    /* allow only numeric keys */
    $('body').on('keypress', '.only-integer', function (evt) {
        return app.isNumericKeyEvent(evt);
    });

    $('body').on('keypress', '.only-decimal', function (evt) {
        return app.isNumericKeyEvent(evt, true);
    });
    $('body').on('keyup', '.only-decimal', function (evt) {
        if (this.value.split('.').length > 2) {
            $(this).val(this.value.substr(0, this.value.indexOf('.', this.value.indexOf('.') + 1)));
        }
    });


    /* form validation */
    $.validator.addMethod('regex', function (value, element, regexObject) {
        return this.optional(element) || regexObject.test(value);
    }, 'Invalid input pattern.');

    $('form.bs-validate').each(function () {
        $(this).validate({
            errorElement: "em",
            errorPlacement: function (error, element) {
                // Add the `help-block` class to the error element
                error.addClass("help-block");
    
                if (element.prop("type") === "checkbox") {
                    error.insertAfter(element.parent("label"));
                } else {
                    error.insertAfter(element);
                }
            },
            highlight: function (element, errorClass, validClass) {
                $(element).parents(".form-group").addClass("has-error").removeClass("has-success");
            },
            unhighlight: function (element, errorClass, validClass) {
                $(element).parents(".form-group").addClass("has-success").removeClass("has-error");
            }
        });
    });

    ///////////////////////////////////////////////////////
    /**
     * Custom bootstrap dropdown menu for checklist.
     * 
     * Sample Markup:
     * 
     *  <div class="dropdown">
     *      <button type="button" class="btn btn-default dropdown-toggle" id="checklistDropdown1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
     *          Dropdown <span class="caret"></span>
     *      </button>
     *      <ul class="dropdown-menu dropdown-menu-checklist" id="field-checklist" aria-labelledby="checklistDropdown1">
     *          <li><a href="#"><input type="checkbox" class="check-input" data-toggle="checklist" value="all" />&nbsp;<strong>ALL</strong></a></li>
     *          <li role="separator" class="divider"></li>
     *          <li><a href="#"><input type="checkbox" class="check-input" value="opt1" />&nbsp;Option1</a></li>
     *          <li><a href="#"><input type="checkbox" class="check-input" value="opt2" />&nbsp;Option2</a></li>
     *      </ul>
     *  </div>
     */
    function getCheckList(element) {
        return $(element).find('a input.check-input:checked').not('[data-toggle="checklist"]').map(function () {
            return this.value;
        }).get();
    }
    function updateMasterInput(element) {
        var $checklist = $(element).find('a input.check-input').not('[data-toggle="checklist"]');
        var $checklistChecked = $(element).find('a input.check-input:checked').not('[data-toggle="checklist"]');
        $(element).find('a input.check-input[data-toggle="checklist"]').prop('checked', $checklist.length == $checklistChecked.length);
    }
    $('.dropdown-menu.dropdown-menu-checklist').each(function (index, element) {
        $(element).css({
            height: 'auto',
            maxHeight: '400px',
            overflowX: 'hidden'
        });

        $(element).find('a').on('click.checklist', function (evt) {
            evt.preventDefault();
            var $checkInput = $(this).find('.check-input');
            $checkInput.prop('checked', !$checkInput.prop('checked')).trigger('change');
            return false;
        }).find('.check-input').on('click.checklist', function (evt) {
            evt.stopPropagation();
            return true;
        });

        $(element).find('a input.check-input').on('change.checklist', function (evt) {
            if ($(this).data('toggle') == 'checklist') {
                $(element).find('a input.check-input').not(this).prop('checked', $(this).prop('checked'));
            } else {
                updateMasterInput(element);
            }
            $(element).trigger('listchange', [getCheckList(element)]);
        });

        $(element).data('setCheckList', function (list) {
            $(element).find('a input.check-input').not('[data-toggle="checklist"]').each(function (index, elem) {
                $(elem).prop('checked', list.indexOf($(elem).val()) > -1);
            });
            updateMasterInput(element);
        });

        $(element).data('getCheckList', function () {
            return getCheckList(element);
        });
    });
    ///////////////////////////////////////////////////////

});


app.toggleListColumns = function (listType, dafaultCols) {
    var colsKey = listType+'_display_cols';
    var storedCols = app.storage.get(colsKey);
    var listCols = storedCols ? JSON.parse(storedCols) : dafaultCols;
    var toggleCols = function (list_cols) {
        $('.toggle-field').each(function (index, element) {
            if (list_cols.indexOf($(element).data('fieldName')) > -1) {
                $(element).show();
            } else {
                $(element).hide();
            }
        });
    };
    toggleCols(listCols);
    $('#field-checklist').on('listchange', function (evt, colsList) {
        toggleCols(colsList);
        $(document.body).find('div#fixed-scrollbar').remove();
        $('.sticky-scrollbar').stickyScroll();
        app.storage.set(colsKey, JSON.stringify(colsList));
    });
    $('#field-checklist').data('setCheckList')(listCols);
};
