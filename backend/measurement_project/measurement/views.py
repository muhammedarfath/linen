from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import CommonOrderDetails, Shirt, Pant, WomensOrderDetails
from .serializers import CommonOrderDetailsSerializer, ShirtSerializer, PantSerializer, WomensOrderDetailsSerializer
from rest_framework.permissions import IsAuthenticated
import logging

class MensMeasurement(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        
        common_order_data = {
            'order_no': data.get('order_no'),
            'name': data.get('name'),
            'saleperson': data.get('saleperson'),
            'phone': data.get('phone'),
            'booking_date': data.get('booking_date'),
            'delivery_date': data.get('delivery_date'),
            'stylist': data.get('stylist'),
            'measurement_master': data.get('measurement_master'),
            'others': data.get('others'),
            'cut_pieces':data.get('Cut_pieces'),
            'bill_invoice_no': data.get('bill_invoice_no'),
            'trial': data.get('trial'),
            'delivery_address': data.get('delivery_address'),
            'image': request.FILES.get('image') 
        }

        # Create CommonOrderDetails instance
        common_order_serializer = CommonOrderDetailsSerializer(data=common_order_data)
        if common_order_serializer.is_valid():
            common_order = common_order_serializer.save()
        else:
            return Response(common_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract Shirt data
        shirt_data = {
            'men_order': common_order.id,
            'length': data.get('length'),
            'shoulder': data.get('shoulder'),
            'full_sleeve': data.get('full_sleeve'),
            'half_sleeve': data.get('half_sleeve'),
            'hs_btm_loose': data.get('hs_btm_loose'),
            'chest': data.get('chest'),
            'stomach': data.get('stomach'),
            'seat': data.get('seat'),
            'a': data.get('a'),
            'b': data.get('b'),
            'c': data.get('c'),
            'neck': data.get('neck'),
            'collar_type': data.get('collar_type'),
            'pocket': data.get('pocket'),
            'reverse_cut_way': data.get('reverse_cut_way'),
            'bottom_line_cut': data.get('bottom_line_cut'),
            'straight_cut': data.get('straight_cut'),
            'slit': data.get('slit'),
            'linen_pady': data.get('linen_pady'),
            'lp_pady': data.get('lp_pady'),
            'cuff': data.get('cuff'),
            'kurtha': data.get('kurtha'),
            'remarks':data.get('remarkshirt')
        }

        shirt_serializer = ShirtSerializer(data=shirt_data)
        if shirt_serializer.is_valid():
            shirt_serializer.save()
        else:
            return Response(shirt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        pant_data = {
            'men_order': common_order.id,
            'full_length': data.get('full_length'),
            'bottom': data.get('bottom'),
            'waist': data.get('waist'),
            'seat': data.get('seat'),
            'loose': data.get('loose'),
            'inside': data.get('inside'),
            'middle': data.get('middle'),
            'fork': data.get('fork'),
            'no_pleat': data.get('no_pleat'),
            'two_pleat': data.get('two_pleat'),
            'cross_pocket': data.get('cross_pocket'),
            'hook': data.get('hook'),
            'side_pocket': data.get('side_pocket'),
            'back_pocket_1': data.get('back_pocket_1'),
            'back_pocket_2': data.get('back_pocket_2'),
            'cu_band': data.get('cu_band'),
            'over_band': data.get('over_band'),
            'band': data.get('band'),
            'button': data.get('button'),
            'remarks': data.get('remarks')
        }

        pant_serializer = PantSerializer(data=pant_data)
        if pant_serializer.is_valid():
            pant_serializer.save()
        else:
            return Response(pant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)




class WomenMeasurement(APIView):
    def post(self, request):
        data = request.data
                
        try:
            common_order_data = {
                "order_no": request.data.get("order_no"),
                "name": request.data.get("name"),
                "saleperson": request.data.get("saleperson"),
                "phone": request.data.get("phone"),
                "booking_date": request.data.get("booking_date"),
                "delivery_date": request.data.get("delivery_date"),
                "stylist": request.data.get("stylist"),
                "measurement_master": request.data.get("measurement_master"),
                "others": request.data.get("others"),
                "bill_invoice_no": request.data.get("bill_invoice_no"),
                "trial": request.data.get("trial"),
                "delivery_address": request.data.get("delivery_address"),
                "image": request.FILES.get('image')
            }

            common_order_serializer = CommonOrderDetailsSerializer(data=common_order_data)

            if common_order_serializer.is_valid():
                common_order = common_order_serializer.save()

                womens_order_data = {
                    "common_order": common_order.id,  
                    "churithar_selected": request.data.get("churithar_selected"),
                    "churithar_quantity": request.data.get("churithar_quantity"),
                    "churithar_description": request.data.get("churithar_description"),
                    "kurthi_selected": request.data.get("kurthi_selected"),
                    "kurthi_quantity": request.data.get("kurthi_quantity"),
                    "kurthi_description": request.data.get("kurthi_description"),
                    "pant_selected": request.data.get("pant_selected"),
                    "pant_quantity": request.data.get("pant_quantity"),
                    "pant_description": request.data.get("pant_description"),
                    "blouse_selected": request.data.get("blouse_selected"),
                    "blouse_quantity": request.data.get("blouse_quantity"),
                    "blouse_description": request.data.get("blouse_description"),
                    "frock_selected": request.data.get("frock_selected"),
                    "frock_quantity": request.data.get("frock_quantity"),
                    "frock_description": request.data.get("frock_description"),
                    "others_selected": request.data.get("others_selected"),
                    "others_quantity": request.data.get("others_quantity"),
                    "others_description": request.data.get("others_description"),
                    "total": request.data.get("total"),
                    "CL": request.data.get("CL"),
                    "WL": request.data.get("WL"),
                    "L": request.data.get("L"),
                    "SH": request.data.get("SH"),
                    "SL": request.data.get("SL"),
                    "SW": request.data.get("SW"),
                    "AH": request.data.get("AH"),
                    "FC": request.data.get("FC"),
                    "CH": request.data.get("CH"),
                    "BR": request.data.get("BR"),
                    "W": request.data.get("W"),
                    "SW2": request.data.get("SW2"),
                    "SE": request.data.get("SE"),
                    "SLIT": request.data.get("SLIT"),
                    "FN": request.data.get("FN"),
                    "BN": request.data.get("BN"),
                    "NW": request.data.get("NW"),
                    "BL": request.data.get("BL"),
                    "BW": request.data.get("BW"),
                    "remarks": request.data.get("remarks"),
                }

                womens_order_serializer = WomensOrderDetailsSerializer(data=womens_order_data)
                if womens_order_serializer.is_valid():
                    womens_order_serializer.save()
                    return Response({"message": "Womens Order Details saved successfully"}, status=status.HTTP_201_CREATED)
                else:
                    return Response(womens_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(common_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class OrderDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        orders = CommonOrderDetails.objects.all()
        data = []

        for order in orders:
            order_data = CommonOrderDetailsSerializer(order).data

            shirt = Shirt.objects.filter(men_order=order).first()
            pant = Pant.objects.filter(men_order=order).first()
            womens_order = WomensOrderDetails.objects.filter(common_order=order).first()

            if shirt:
                order_data['shirt_details'] = ShirtSerializer(shirt).data
            if pant:
                order_data['pant_details'] = PantSerializer(pant).data
            if womens_order:
                order_data['womens_order_details'] = WomensOrderDetailsSerializer(womens_order).data

            data.append(order_data)

        return Response(data, status=status.HTTP_200_OK)
    
    
class OrderCountView(APIView):
    def get(self, request, *args, **kwargs):
        total_count = CommonOrderDetails.objects.count()
        return Response({'count': total_count}, status=status.HTTP_200_OK) 
    
    
    
class UpdateOrderStatusView(APIView):
    def put(self, request, order_id):
        try:
            order = CommonOrderDetails.objects.get(id=order_id)
        except CommonOrderDetails.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        status_update = request.data.get("status")
        if status_update:
            order.status = status_update
            order.save()
            serializer = CommonOrderDetailsSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)   
        
        
        
logger = logging.getLogger(__name__)

class OrderDetailUpdateView(APIView):
    def put(self, request, order_id):
        try:
            common_order = CommonOrderDetails.objects.get(id=order_id)
        except CommonOrderDetails.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        common_order_data = {
            'order_no': request.data.get('order_no', common_order.order_no),
            'name': request.data.get('name', common_order.name),
            'saleperson': request.data.get('saleperson', common_order.saleperson),
            'phone': request.data.get('phone', common_order.phone),
            'booking_date': request.data.get('booking_date', common_order.booking_date),
            'delivery_date': request.data.get('delivery_date', common_order.delivery_date),
            'stylist': request.data.get('stylist', common_order.stylist),
            'measurement_master': request.data.get('measurement_master', common_order.measurement_master),
            'others': request.data.get('others', common_order.others),
            'bill_invoice_no': request.data.get('bill_invoice_no', common_order.bill_invoice_no),
            'trial': request.data.get('trial', common_order.trial),
            'delivery_address': request.data.get('delivery_address', common_order.delivery_address),
        }

        common_order_serializer = CommonOrderDetailsSerializer(common_order, data=common_order_data, partial=True)
        if common_order_serializer.is_valid():
            common_order_serializer.save()
        else:
            logger.error(f"CommonOrderDetailsSerializer errors: {common_order_serializer.errors}")
            return Response(common_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        shirt_data = request.data.get('shirt', {})
        if shirt_data:
            try:
                shirt = Shirt.objects.get(men_order=common_order)
                shirt_serializer = ShirtSerializer(shirt, data=shirt_data, partial=True)
                if shirt_serializer.is_valid():
                    shirt_serializer.save()
                else:
                    logger.error(f"ShirtSerializer errors: {shirt_serializer.errors}")
                    return Response(shirt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Shirt.DoesNotExist:
                return Response({"error": "Shirt details not found"}, status=status.HTTP_404_NOT_FOUND)
        
        pant_data = request.data.get('pant', {})
        if pant_data:
            try:
                pant = Pant.objects.get(men_order=common_order)
                pant_serializer = PantSerializer(pant, data=pant_data, partial=True)
                if pant_serializer.is_valid():
                    pant_serializer.save()
                else:
                    logger.error(f"PantSerializer errors: {pant_serializer.errors}")
                    return Response(pant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Pant.DoesNotExist:
                return Response({"error": "Pant details not found"}, status=status.HTTP_404_NOT_FOUND)

        womens_order_data = request.data.get('womens_order', {})
        if womens_order_data:
            try:
                womens_order = WomensOrderDetails.objects.get(common_order=common_order)
                womens_order_serializer = WomensOrderDetailsSerializer(womens_order, data=womens_order_data, partial=True)
                if womens_order_serializer.is_valid():
                    womens_order_serializer.save()
                else:
                    logger.error(f"WomensOrderDetailsSerializer errors: {womens_order_serializer.errors}")
                    return Response(womens_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except WomensOrderDetails.DoesNotExist:
                return Response({"error": "WomensOrderDetails not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Order details updated successfully"}, status=status.HTTP_200_OK)