import serial
import serial.tools.list_ports
import time
import sys

# ============== 설정 ==============
INPUT_PORT = "COM10"      # STM32 연결 포트 (수신)
OUTPUT_PORT = "COM8"     # 출력 포트 (송신)
BAUD_RATE = 115200       # 통신 속도
# ==================================

def list_available_ports():
    """사용 가능한 시리얼 포트 목록 출력"""
    ports = serial.tools.list_ports.comports()
    print("\n[사용 가능한 시리얼 포트]")
    if not ports:
        print("  포트를 찾을 수 없습니다.")
    for port in ports:
        print(f"  {port.device}: {port.description}")
    print()

def serial_bridge():
    """시리얼 포트 브릿지 메인 함수"""
   
    list_available_ports()
   
    input_serial = None
    output_serial = None
   
    try:
        # 입력 포트 연결 (STM32)
        print(f"입력 포트 연결 중: {INPUT_PORT}")
        input_serial = serial.Serial(
            port=INPUT_PORT,
            baudrate=BAUD_RATE,
            timeout=0.1
        )
        print(f"  ✓ {INPUT_PORT} 연결 성공")
       
        # 출력 포트 연결
        print(f"출력 포트 연결 중: {OUTPUT_PORT}")
        output_serial = serial.Serial(
            port=OUTPUT_PORT,
            baudrate=BAUD_RATE,
            timeout=0.1
        )
        print(f"  ✓ {OUTPUT_PORT} 연결 성공")
       
        print("\n" + "="*50)
        print("시리얼 브릿지 시작")
        print(f"  {INPUT_PORT} → {OUTPUT_PORT}")
        print("종료: Ctrl+C")
        print("="*50 + "\n")
       
        valid_commands = {'W', 'A', 'S', 'D', 'X', 'Y', 'U', 'I' }
       
        while True:
            # 입력 포트에서 데이터 수신
            if input_serial.in_waiting > 0:
                data = input_serial.readline().decode('utf-8', errors='ignore').strip()
               
                if data:
                    # 유효한 명령어인지 확인
                    if data in valid_commands:
                        # 출력 포트로 전송
                        output_serial.write(f"{data}\n".encode('utf-8'))
                        print(f"[전송] {data}")
                    else:
                        # 디버그 메시지는 화면에만 표시
                        print(f"[수신] {data}")
           
            time.sleep(0.001)  # CPU 부하 감소
           
    except serial.SerialException as e:
        print(f"\n[오류] 시리얼 포트 오류: {e}")
    except KeyboardInterrupt:
        print("\n\n프로그램 종료")
    finally:
        if input_serial and input_serial.is_open:
            input_serial.close()
            print(f"{INPUT_PORT} 닫힘")
        if output_serial and output_serial.is_open:
            output_serial.close()
            print(f"{OUTPUT_PORT} 닫힘")

if __name__ == "__main__":
    serial_bridge()