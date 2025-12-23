set(IDF_TARGET esp32p4)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    ${MICROPY_BOARD_DIR}/sdkconfig.p4_kaki5
)
